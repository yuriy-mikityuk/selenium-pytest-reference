from selenium.webdriver.common.by import By

from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage


class SubmittedFormPage(BasePage):
    _MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        super().__init__(driver)

        self.received_text = BaseElement(driver, self._MESSAGE)

