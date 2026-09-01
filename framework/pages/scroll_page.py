from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class ScrollPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/scroll3.html"
    _BUTTON_1 = (By.ID, "button1")
    _BUTTON_2 = (By.ID, "button2")

    def __init__(self, driver):
        super().__init__(driver)
        self.button1 = BaseElement(self.driver, self._BUTTON_1)
        self.button2 = BaseElement(self.driver, self._BUTTON_2)

    def scroll_to_button_2_with_actions(self):
        element_to_scroll = self.button2.wait_until_displayed()
        ActionChains(self.driver).scroll_to_element(element_to_scroll).perform()

    def scroll_by_amount(self, delta_y, timeout=5):
        current_y = self.execute_script("return window.scrollY;")
        expected_y = current_y + delta_y

        ActionChains(self.driver).scroll_by_amount(
            delta_x=0,
            delta_y=delta_y,
        ).perform()

        WebDriverWait(self.driver, timeout).until(
            lambda _: self.execute_script("return window.scrollY;") == expected_y
        )

    def scroll_from_origin(
            self,
            origin_element,
            delta_x,
            delta_y,
            timeout=5,
    ):
        current_y = self.execute_script("return window.scrollY;")
        web_element = origin_element.wait_until_displayed()
        origin = ScrollOrigin.from_element(web_element)

        ActionChains(self.driver).scroll_from_origin(
            scroll_origin=origin,
            delta_x=delta_x,
            delta_y=delta_y,
        ).perform()

        WebDriverWait(self.driver, timeout).until(
            lambda _: self.execute_script("return window.scrollY;") != current_y
        )

