from selenium.webdriver.common.by import By
import os
import sys

from framework.elements.dropdown import Dropdown
from framework.elements.text_input import TextInput
from framework.elements.button import Button
from framework.pages.base_page import BasePage
from framework.pages.submitted_form_page import SubmittedFormPage
from framework.elements.checkbox import Checkbox
from framework.elements.radio_button import RadioButton
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from framework.elements.base_element import BaseElement
from selenium.webdriver.support.relative_locator import locate_with


class WebFormPage(BasePage):

    URL = "https://www.selenium.dev/selenium/web/web-form.html"
    _TEXT_INPUT = (By.ID, "my-text-id")
    _SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    _DROPDOWN_OPTIONS = (By.XPATH, "//select[@name='my-select']")
    _CHECKED_CHECKBOX = (By.XPATH, "//input[@id='my-check-1']")
    _DEFAULT_CHECKBOX = (By.XPATH, "//input[@id='my-check-2']")
    _CHECKED_RADIO_BUTTON = (By.XPATH, "//input[@id='my-radio-1']")
    _DEFAULT_RADIO_BUTTON = (By.XPATH, "//input[@id='my-radio-2']")
    _TEXT_AREA = (By.XPATH, '//*[@name="my-textarea"]')
    _FILE_INPUT = (By.XPATH, "//input[@name='my-file']")
    _RETURN_TO_INDEX_LINK = (By.LINK_TEXT, "Return to index")
    _DISABLED_INPUT = (By.XPATH, "//input[@name='my-disabled']")
    _READONLY_INPUT = (By.XPATH, "//input[@name='my-readonly']")

    def __init__(self, driver):
        super().__init__(driver)

        self.text_input = TextInput(driver, self._TEXT_INPUT)
        self.submit_button = Button(driver, self._SUBMIT_BUTTON)
        self.dropdown_options = Dropdown(driver, self._DROPDOWN_OPTIONS)
        self.default_checkbox = Checkbox(driver, self._DEFAULT_CHECKBOX)
        self.checked_checkbox = Checkbox(driver, self._CHECKED_CHECKBOX)

        self.checked_radio = RadioButton(driver, self._CHECKED_RADIO_BUTTON)
        self.default_radio = RadioButton(driver, self._DEFAULT_RADIO_BUTTON)
        self.text_area = TextInput(driver, self._TEXT_AREA)
        self.file_input = TextInput(driver, self._FILE_INPUT)
        self.return_to_index_link = BaseElement(driver, self._RETURN_TO_INDEX_LINK)
        self.disabled_input = TextInput(driver, self._DISABLED_INPUT)
        self.readonly_input = TextInput(driver, self._READONLY_INPUT)

    def submit(self):
        self.submit_button.click()
        return SubmittedFormPage(self.driver)

    def send_keys_to_text_area(self, keys):
        action = ActionChains(self.driver)
        action.send_keys_to_element(self.text_area.wait_until_displayed(), keys).perform()

    def type_uppercase_text(self, text):
        (ActionChains(self.driver)
         .key_down(Keys.SHIFT)
         .send_keys_to_element(self.text_area.wait_until_displayed(), text)
         .key_up(Keys.SHIFT)
         .perform())

    def upload_file(self, file_path):
        file_path = os.path.abspath(file_path)

        self.file_input.wait_until_displayed()
        self.file_input.send_keys(file_path)

    def select_all_and_replace(self, new_text):
        modifier = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        (ActionChains(self.driver)
        .click(self.text_input.wait_until_displayed())
        .key_down(modifier)
        .send_keys("a")
        .key_up(modifier)
        .send_keys(Keys.BACKSPACE)
        .send_keys(new_text)
        .perform())

    def get_password_input_attribute(self, attribute_name):
        text_elem = self.text_input.wait_until_displayed()
        password_elem = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(text_elem)
        )
        return password_elem.get_attribute(attribute_name)







