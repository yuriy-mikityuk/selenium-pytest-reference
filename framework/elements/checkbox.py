from framework.elements.base_element import BaseElement

class Checkbox(BaseElement):
    def check(self):
        self.wait_until_clickable().click()

    def is_checked(self):
        return self.find_element().is_selected()

    def set_checked(self):
        if not self.is_checked():
            self.check()