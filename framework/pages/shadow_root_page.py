from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class ShadowRootPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/shadowRootPage.html"
    _SHADOW_HOST = (By.CSS_SELECTOR, "custom-checkbox-element")

    def get_shadow_checkbox(self):
        shadow_host = self.driver.find_element(*self._SHADOW_HOST)
        shadow_root = shadow_host.shadow_root
        return shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
