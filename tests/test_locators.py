from playwright.async_api import Page, expect
import re, time

class login:

# CSS Selector
    def __init__(self):
        page=Page
        # self.fullName =page.locator('#userName') -- #: ID
        # self.title = page.locator('.text-center') -- . :class
        # self.placeholderFN = page.locator("[placeholder='Full Name']") -- [] : tìm theo thuộc tính ất kì
        # self.email = page.locator('div>input')-- > : tìm thẻ p nằm trong thẻ div


        self.fullName = page.get_by_placeholder("Full Name")
        

