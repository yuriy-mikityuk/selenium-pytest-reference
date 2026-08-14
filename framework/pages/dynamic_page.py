from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from framework.elements.text_input import TextInput
from framework.elements.button import Button
from framework.pages.base_page import BasePage

class DynamicPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/dynamic.html"

    _ADD_BOX_BUTTON = (By.ID, "adder")
    _REVEAL_BUTTON = (By.ID, "reveal")
    _REVEALED_INPUT = (By.ID, "revealed")
    _ALL_BOXES = (By.CSS_SELECTOR, "[id^='box']")

    def __init__(self, driver):
        super().__init__(driver)

        self.add_box_button = Button(driver, self._ADD_BOX_BUTTON)
        self.reveal_button = Button(driver, self._REVEAL_BUTTON)
        self.revealed_input = TextInput(driver, self._REVEALED_INPUT)

    def add_box(self):
        count_before = self.get_boxes_count()
        self.add_box_button.click()
        self.wait_until_boxes_count(expected_count=count_before + 1)

    def get_boxes_count(self):
        return len(self.driver.find_elements(*self._ALL_BOXES))

    def reveal_input(self):
        self.reveal_button.click()
        self.revealed_input.wait_until_displayed()

    def wait_until_boxes_count(self, expected_count, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda _: self.get_boxes_count() == expected_count)




