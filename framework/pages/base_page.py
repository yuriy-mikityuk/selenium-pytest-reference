from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.browser.cookie_manager import CookieManager
from typing import ClassVar

class BasePage:
    URL: ClassVar[str]

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cookies = CookieManager(driver)

    def open(self):
        self.driver.get(self.URL)

    def close_current_window(self):
        self.driver.close()

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_to_frame(self, frame_reference, timeout=10):
        WebDriverWait(self.driver, timeout=timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def take_screenshot(self, file_path: str) -> bool:
        return self.driver.save_screenshot(file_path)

    def get_screenshot_as_png(self) -> bytes:
        return self.driver.get_screenshot_as_png()

    def print_page(self, print_options=None):
        return self.driver.print_page(print_options=print_options)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()
