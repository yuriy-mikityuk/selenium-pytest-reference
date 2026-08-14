from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def click(self):
        # TODO: LOGGER
        self.wait_until_clickable().click()

    def find_element(self):
        return self.driver.find_element(*self.locator)

    def is_displayed(self):
        return self.find_element().is_displayed()

    def wait_until_displayed(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.locator))

    def wait_until_clickable(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.locator))

    def get_property(self, property_name):
        return self.find_element().get_property(property_name)

    def get_text(self):
        return self.wait_until_displayed().text