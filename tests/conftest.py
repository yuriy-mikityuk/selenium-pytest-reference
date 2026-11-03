import base64
import re
from collections.abc import Callable

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from framework.pages.dynamic_page import DynamicPage
from framework.pages.web_form_page import WebFormPage
from framework.pages.alerts_page import AlertsPage
from framework.pages.windows_page import WindowsPage
from framework.pages.mouse_interaction_page import MouseInteractionPage
from framework.pages.scroll_page import ScrollPage
from framework.pages.shadow_root_page import ShadowRootPage
from framework.pages.pen_pages import PenPage
from framework.pages.bidi_logging_page import BidiLoggingPage
from framework.pages.bidi_network_page import BidiNetworkPage

DriverFactory = Callable[..., WebDriver]
WebFormFactory = Callable[[], WebFormPage]

BROWSERS = {
    "chrome": (webdriver.Chrome, webdriver.ChromeOptions, ["start-maximized", "--headless"]),
    "firefox": (webdriver.Firefox, webdriver.FirefoxOptions, ["-headless"]),
}

# Every driver a test started, whichever fixture started it. The failure hook
# reads this instead of item.funcargs, which misses factory-made drivers.
DRIVERS_KEY = pytest.StashKey[list[WebDriver]]()


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", default="chrome", choices=sorted(BROWSERS), help="browser for the UI tests")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    browser = config.getoption("--browser")
    for item in items:
        item.add_marker("api" if item.path.parent.name == "api" else "ui")
        chrome_only = item.get_closest_marker("chrome_only")
        if chrome_only and browser != "chrome":
            item.add_marker(pytest.mark.skip(reason=chrome_only.args[0]))


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item: pytest.Item):
    report = yield
    # "setup" covers failures in page fixtures, "call" the test body. Both come
    # before the driver teardown, so the browser is still alive at this point.
    if report.failed and report.when in ("setup", "call"):
        attach_screenshots(item, report)
    return report


def attach_screenshots(item: pytest.Item, report: pytest.TestReport) -> None:
    directory = item.config.rootpath / "artifacts" / "screenshots"
    directory.mkdir(parents=True, exist_ok=True)
    test_name = re.sub(r"[^\w.-]+", "_", item.nodeid)
    report.extras = getattr(report, "extras", [])

    for index, driver in enumerate(item.stash.get(DRIVERS_KEY, [])):
        try:
            png = driver.get_screenshot_as_png()
        except Exception as error:
            # Open alert, dead session, crashed driver. An exception escaping a
            # hook aborts the whole run, and the test failure matters more.
            report.sections.append(("screenshot", f"driver {index}: not taken, {error!r}"))
            continue
        path = directory / f"{test_name}-{index}.png"
        path.write_bytes(png)
        report.sections.append(("screenshot", str(path)))
        report.extras.append(extras.png(base64.b64encode(png).decode(), name=path.name))


@pytest.fixture(scope="session")
def browser_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--browser")


# Drivers stay function-scoped on purpose. Tests leave cookies, open windows and
# virtual authenticators behind, and a fresh browser costs about a second.
@pytest.fixture()
def driver_factory(request: pytest.FixtureRequest, browser_name: str) -> DriverFactory:
    def create_driver(bidi: bool = False) -> WebDriver:
        driver_class, options_class, arguments = BROWSERS[browser_name]
        options = options_class()
        for argument in arguments:
            options.add_argument(argument)
        if bidi:
            options.enable_bidi = True

        browser = driver_class(options=options)
        request.addfinalizer(browser.quit)
        request.node.stash.setdefault(DRIVERS_KEY, []).append(browser)
        return browser

    return create_driver


@pytest.fixture()
def driver(driver_factory: DriverFactory) -> WebDriver:
    return driver_factory()


@pytest.fixture()
def bidi_driver(driver_factory: DriverFactory) -> WebDriver:
    return driver_factory(bidi=True)


@pytest.fixture()
def dynamic_page(driver):
    dynamic_page = DynamicPage(driver)
    dynamic_page.open()
    return dynamic_page


@pytest.fixture()
def web_form_page(driver):
    web_form_page = WebFormPage(driver)
    web_form_page.open()
    return web_form_page


@pytest.fixture()
def web_form_factory(driver_factory: DriverFactory) -> WebFormFactory:
    def create_page() -> WebFormPage:
        page = WebFormPage(driver_factory())
        page.open()
        return page

    return create_page


@pytest.fixture()
def alerts_page(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    return alerts_page


@pytest.fixture()
def windows_page(driver):
    windows_page = WindowsPage(driver)
    windows_page.open()
    return windows_page


@pytest.fixture()
def mouse_interaction_page(driver):
    mouse_interaction_page = MouseInteractionPage(driver)
    mouse_interaction_page.open()
    return mouse_interaction_page


@pytest.fixture()
def scroll_page(driver):
    scroll_page = ScrollPage(driver)
    scroll_page.open()
    return scroll_page


@pytest.fixture()
def shadow_root_page(driver):
    shadow_root_page = ShadowRootPage(driver)
    shadow_root_page.open()
    return shadow_root_page


@pytest.fixture()
def pen_page(driver):
    page = PenPage(driver)
    page.open()
    return page


@pytest.fixture()
def bidi_logging_page(bidi_driver):
    page = BidiLoggingPage(bidi_driver)
    page.open()
    return page


# BiDi network interception runs on Chrome and Firefox, but pages must be
# opened with open_via_bidi(). ChromeDriver runs forwarded BiDi commands such as
# network.continueRequest on the session thread, behind the classic command in
# progress, so driver.get() with an active intercept hangs until the page load
# timeout ("Timed out receiving message from renderer").
# https://issues.chromium.org/issues/425906330
@pytest.fixture()
def bidi_network_page(bidi_driver) -> BidiNetworkPage:
    return BidiNetworkPage(bidi_driver)
