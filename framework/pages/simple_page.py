from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.base_element import BaseElement


class SimplePage(BasePage):
    _PAGE_TEXT = (By.XPATH, "//div")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_text = (
            BaseElement(self.driver, self._PAGE_TEXT)
        )
