from framework.elements.base_element import BaseElement


class Button(BaseElement):

    def click(self):
        # TODO: LOGGER
        self.wait_until_clickable().click()