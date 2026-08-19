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

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def get_cookies(self):
        return self.driver.get_cookies()

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()



