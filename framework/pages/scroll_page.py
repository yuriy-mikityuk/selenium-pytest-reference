from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ScrollPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/scroll3.html"
    _BUTTON_1 = (By.ID, "button1")
    _BUTTON_2 = (By.ID, "button2")

    def __init__(self, driver):
        super().__init__(driver)
        self.button1 = BaseElement(self.driver, self._BUTTON_1)
        self.button2 = BaseElement(self.driver, self._BUTTON_2)
