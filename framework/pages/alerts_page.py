from selenium.webdriver.common.by import By
from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage


class AlertsPage(BasePage):
    URL = 'https://www.selenium.dev/selenium/web/alerts.html'

    _SIMPLE_ALERT_TRIGGER = (By.ID, "alert")

    def __init__(self, driver):
        super().__init__(driver)

        self.simple_alert_trigger = BaseElement(
            driver,
            self._SIMPLE_ALERT_TRIGGER,
        )