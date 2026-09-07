from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver


class CookieManager:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def set(self, name: str, value: str) -> None:
        self.add_cookie({"name": name, "value": value})

    def get(self, name: str) -> str | None:
        cookie = self.get_cookie(name)
        if cookie is None:
            return None
        cookie_value = cookie.get("value")
        return cookie_value

    def delete(self, name: str) -> None:
        self.driver.delete_cookie(name)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def get_cookie(self, name):
        """Return the full cookie, including its attributes, or None."""
        return self.driver.get_cookie(name)

    def get_cookies(self):
        return self.driver.get_cookies()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()
