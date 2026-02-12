from playwright.async_api import Page, expect
import re, time

def test_check_title_google(page: Page):
    print("Navigate to Google page...")
    page.goto("https://www.google.com/")
    time.sleep(10)