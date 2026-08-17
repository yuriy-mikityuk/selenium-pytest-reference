from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from framework.elements.base_element import BaseElement

class MouseInteractionPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/mouse_interaction.html"
    _HOVER_AREA = (By.ID, "hover")
    _STATUS = (By.XPATH, "//*[@id='move-status']")
    _DRAGGABLE = (By.ID, "draggable")
    _DROPPABLE = (By.ID, "droppable")
    _DROPPED_TEXT = (By.ID, "drop-status")
    _CLICKABLE = (By.ID, "clickable")
    _CLICK_STATUS = (By.ID, "click-status")


    def __init__(self, driver):
        super().__init__(driver)

        self.hover_area = BaseElement(self.driver, self._HOVER_AREA)
        self.status = BaseElement(self.driver, self._STATUS)
        self.draggable = BaseElement(self.driver, self._DRAGGABLE)
        self.droppable = BaseElement(self.driver, self._DROPPABLE)
        self.dropped_text = BaseElement(self.driver, self._DROPPED_TEXT)
        self.clickable = BaseElement(self.driver, self._CLICKABLE)
        self.click_status = BaseElement(self.driver, self._CLICK_STATUS)

    def hover_over_area(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.hover_area.wait_until_displayed()).perform()

    def drag_and_drop(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.draggable.wait_until_displayed(), self.droppable.wait_until_displayed()).perform()

    def drag_and_drop_by_actions(self):
        (ActionChains(self.driver).click_and_hold(self.draggable.wait_until_displayed())
         .move_to_element(self.droppable.wait_until_displayed()).release().perform())

    def context_click_element(self):
        action = ActionChains(self.driver)
        action.context_click(self.clickable.wait_until_displayed()).perform()

    def double_click_element(self):
        action = ActionChains(self.driver)
        action.double_click(self.clickable.wait_until_displayed()).perform()
