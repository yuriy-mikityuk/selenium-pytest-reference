from framework.elements.base_element import BaseElement


class TextInput(BaseElement):

    def send_keys(self, text):
        element = self.wait_until_clickable()
        self._log_action(f"send_keys({text!r})")
        element.send_keys(text)

    def get_value(self):
        return self.get_property("value")

    def fill(self, text):
        element = self.wait_until_clickable()
        self._log_action(f"fill({text!r})")
        element.clear()
        element.send_keys(text)
