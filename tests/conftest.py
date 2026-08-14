import pytest
from selenium import webdriver

from framework.pages.dynamic_page import DynamicPage
from framework.pages.web_form_page import WebFormPage


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


