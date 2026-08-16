from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

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
