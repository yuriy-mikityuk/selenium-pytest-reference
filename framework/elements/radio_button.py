from framework.elements.base_element import BaseElement

class RadioButton(BaseElement):
    def select(self):
        if not self.is_selected():
            self.click()
