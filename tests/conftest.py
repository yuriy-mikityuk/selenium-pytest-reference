import pytest
from selenium import webdriver

from framework.pages.dynamic_page import DynamicPage
from framework.pages.web_form_page import WebFormPage
from framework.pages.alerts_page import AlertsPage
from framework.pages.windows_page import WindowsPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.browser_version = "stable"
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




