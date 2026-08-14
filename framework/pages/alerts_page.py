from selenium.webdriver.common.by import By
from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage(BasePage):
    URL = 'https://www.selenium.dev/selenium/web/alerts.html'

    _SIMPLE_ALERT_TRIGGER = (By.ID, "alert")
    _CONFIRM_ALERT_TRIGGER = (By.ID, "confirm")

    def __init__(self, driver):
        super().__init__(driver)

        self.simple_alert_trigger = BaseElement(
            driver,
            self._SIMPLE_ALERT_TRIGGER,
        )
        self.confirm_alert_trigger = BaseElement(
            driver,
            self._CONFIRM_ALERT_TRIGGER,
        )

    def open_simple_alert(self):
        self.simple_alert_trigger.click()
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())


    def open_confirm_alert(self):
        self.confirm_alert_trigger.click()
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())