from framework.elements.base_element import BaseElement

class Checkbox(BaseElement):
    def is_checked(self):
        return self.find_element().is_selected()

    def set_checked(self, should_be_checked):
        if self.is_checked() != should_be_checked:
            self.click()
