import pytest
from selenium import webdriver

from framework.pages.dynamic_page import DynamicPage
from framework.pages.web_form_page import WebFormPage
from framework.pages.alerts_page import AlertsPage
from framework.pages.windows_page import WindowsPage
from framework.pages.mouse_interaction_page import MouseInteractionPage
from framework.pages.scroll_page import ScrollPage
from framework.pages.shadow_root_page import ShadowRootPage

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.browser_version = "stable"
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






