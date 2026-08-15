from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.base_element import BaseElement


class SimplePage(BasePage):
    _TEXT_IN_NEW_WINDOW = (By.XPATH, "//div")

    def __init__(self, driver):
        super().__init__(driver)
        self.text_in_new_window = (
            BaseElement(self.driver, self._TEXT_IN_NEW_WINDOW)
        )