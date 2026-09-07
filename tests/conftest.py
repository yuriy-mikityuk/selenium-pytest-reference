import pytest
from selenium import webdriver

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

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.browser_version = "stable"
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

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
def driver_factory(request):

    def create_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        request.addfinalizer(browser.quit)
        return browser

    return create_driver

@pytest.fixture()
def web_form_factory(driver_factory):
    def create_page():
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
def bidi_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.enable_bidi = True


    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture()
def bidi_logging_page(bidi_driver):
    page = BidiLoggingPage(bidi_driver)
    page.open()
    return page


# Firefox is used for BiDi network interception: in Chrome, a classic
# navigation (driver.get) that waits for a BiDi command response deadlocks.
# Affects both network.continueRequest and network.continueWithAuth.
#
# Symptom: driver.get() blocks until the page load timeout, then raises
#   TimeoutException: timeout: Timed out receiving message from renderer
#
# Verified 2026-09-02 on Chrome 152.0.7977.65 / ChromeDriver 152.0.7977.75 /
# Selenium 4.46.0. Both auth styles fail identically (add_auth_handler and
# add_authentication_handler), so this is the interception phase, not the API.
#
# TODO: switch these fixtures back to Chrome once fixed — check by running
# the BiDi tests against a Chrome driver with enable_bidi.
# https://issues.chromium.org/issues/425906330
@pytest.fixture()
def firefox_bidi_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    options.enable_bidi = True

    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()

@pytest.fixture()
def firefox_bidi_network_page(firefox_bidi_driver):
    return BidiNetworkPage(firefox_bidi_driver)




