from framework.elements.button import Button
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.pages.simple_page import SimplePage


class WindowsPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/window_switching_tests/page_with_frame.html"

    _LINK_TO_NEW_WINDOW = (By.ID, "a-link-that-opens-a-new-window")

    def __init__(self, driver):
        super().__init__(driver)

        self.link_to_new_window = Button(driver, self._LINK_TO_NEW_WINDOW)

    def current_window_handle(self):
        return self.driver.current_window_handle

    def open_new_window(self):
        current_window = self.driver.current_window_handle
        number_of_windows = self.get_number_of_windows()

        self.link_to_new_window.click()
        self.wait_for_window_handles(number_of_windows + 1)

        new_window = next(
            handle
            for handle in self.driver.window_handles
            if handle != current_window
        )
        self.driver.switch_to.window(new_window)
        return SimplePage(self.driver)

    # дождаться n количество window_handles
    def wait_for_window_handles(self, n):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(n))

    def get_number_of_windows(self):
        return len(self.driver.window_handles)
