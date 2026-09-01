from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_PEN
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.remote.webdriver import WebDriver

from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PenPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/pointerActionsPage.html"

    _POINTER_AREA  = (By.ID,"pointerArea")
    _POINTER_DOWN = (By.CLASS_NAME, "pointerdown")
    _SECOND_POINTER_MOVE = (
        By.XPATH,
        "(//*[@class='pointermove'])[2]",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.pointer_area = BaseElement(self.driver, self._POINTER_AREA)
        self.pointer_down = BaseElement(self.driver, self._POINTER_DOWN)
        self.second_pointer_move = BaseElement(self.driver, self._SECOND_POINTER_MOVE)

    def draw_with_pen(self, tilt_x=None, tilt_y=None, twist=None):
        pointer_area_element = self.pointer_area.wait_until_displayed()
        pen_input = PointerInput(POINTER_PEN, "default pen")
        actions = ActionBuilder(self.driver, pen_input)
        (
            actions.pointer_action
            .move_to(pointer_area_element)
            .pointer_down()
            .move_by(2, 2, tilt_x=tilt_x, tilt_y=tilt_y, twist=twist)
            .pointer_up()
        )

        actions.perform()