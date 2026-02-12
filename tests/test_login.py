from pages.login_page import LoginBasePage as LoginPage 
from playwright.async_api import Page, expect

def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.visit_login_page()
    login_page.login("admin_example", "123456")

def test_login_failed_with_invalid_username(page: Page):
    login_page = LoginPage(page)
    login_page.visit_login_page()
    login_page.login("invalid_user", "123456")
    login_page.assert_text_visible(login_page.error_message, "Invalid credentials")