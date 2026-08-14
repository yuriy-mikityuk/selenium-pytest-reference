from selenium.webdriver.common.by import By

from framework.elements.dropdown import Dropdown
from framework.elements.text_input import TextInput
from framework.elements.button import Button
from framework.pages.base_page import BasePage
from framework.pages.submitted_form_page import SubmittedFormPage
from framework.elements.checkbox import Checkbox
from framework.elements.radio_button import RadioButton

class WebFormPage(BasePage):

    URL = "https://www.selenium.dev/selenium/web/web-form.html"
    _TEXT_INPUT = (By.ID, "my-text-id")
    _SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    _DROPDOWN_OPTIONS = (By.XPATH, "//select[@name='my-select']")
    _CHECKED_CHECKBOX = (By.XPATH, "//input[@id='my-check-1']")
    _DEFAULT_CHECKBOX = (By.XPATH, "//input[@id='my-check-2']")
    _CHECKED_RADIO_BUTTON = (By.XPATH, "//input[@id='my-radio-1']")
    _DEFAULT_RADIO_BUTTON = (By.XPATH, "//input[@id='my-radio-2']")

    def __init__(self, driver):
        super().__init__(driver)

        self.text_input = TextInput(driver, self._TEXT_INPUT)
        self.submit_button = Button(driver, self._SUBMIT_BUTTON)
        self.dropdown_options = Dropdown(driver, self._DROPDOWN_OPTIONS)
        self.default_checkbox = Checkbox(driver, self._DEFAULT_CHECKBOX)
        self.checked_checkbox = Checkbox(driver, self._CHECKED_CHECKBOX)

        self.checked_radio = RadioButton(driver, self._CHECKED_RADIO_BUTTON)
        self.default_radio = RadioButton(driver, self._DEFAULT_RADIO_BUTTON)

    def submit(self):
        self.submit_button.click()
        return SubmittedFormPage(self.driver)








