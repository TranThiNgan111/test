from pages.base_page import BasePage
from playwright.async_api import expect, Playwright

class Home(BasePage):
    Btn_Clockin = ""
    Btn_Clockout = ""
    search_box =""
    #liệt kê toàn bộ element có trên trang

    #thực hiện test:
    def test_verify_ClockinButton_Visibale(self, text: str):
        self._select_menu("Home")
        assert text == "Display"