from playwright.async_api import Page, expect
import re, time

def test_login(page: Page):
    print("Login...")
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill ("standard_user")
    page.get_by_placeholder("Password").fill ("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()

