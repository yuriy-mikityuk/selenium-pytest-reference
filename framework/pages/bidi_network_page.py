from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from framework.elements.base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait

class BidiNetworkPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/blank.html"