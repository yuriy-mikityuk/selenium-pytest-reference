from framework.elements.base_element import BaseElement
from selenium.webdriver.support.ui import Select

class Dropdown(BaseElement):

    def choose_option_in_dropdown(self, option_text):
        Select(self.wait_until_clickable()).select_by_visible_text(option_text)

    def read_actual_dropdown(self):
        selected_option = Select(self.wait_until_clickable()).first_selected_option
        return selected_option.text