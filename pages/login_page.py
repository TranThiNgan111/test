from .base_page import BasePage
from playwright.async_api import expect, Playwright
import time

class LoginBasePage(BasePage):
    URL = "https://hrm.anhtester.com/"
    Username= "#iusername"
    Password= "#ipassword"
    BtnLogin= "//button[contains(@class, 'btn-primary')]"

    def __init__(self, page):
        super().__init__(page)

    def visit_login_page(self,playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        self._visit(self.URL)

    def login(self, username: str, password: str):
        self.visit_login_page()
        self._fill(self.Username, username, "Username Input")
        self._fill(self.Password, password, "Password Input")
        self._click(self.BtnLogin, "Login Button")
        time.sleep(5)