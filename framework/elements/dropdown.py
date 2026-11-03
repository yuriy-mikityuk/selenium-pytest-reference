from framework.elements.base_element import BaseElement
from selenium.webdriver.support.ui import Select

class Dropdown(BaseElement):

    def choose_option_in_dropdown(self, option_text):
        select = Select(self.wait_until_clickable())
        self._log_action(f"choose_option_in_dropdown({option_text!r})")
        select.select_by_visible_text(option_text)

    def read_actual_dropdown(self):
        selected_option = Select(self.wait_until_clickable()).first_selected_option
        return self._log_result("read_actual_dropdown", selected_option.text)
