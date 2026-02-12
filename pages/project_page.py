from pages.base_page import BasePage
from playwright.async_api import expect

class Project(BasePage):
    Btn_Clockin = ""
    Btn_Clockout = ""
    search_box =""
    #liệt kê toàn bộ element có trên trang

    #thực hiện test:
    def test_select_project_menu(self, text: str):
        self._select_menu("Project")
        assert text == "Display"

    def test_search_function(self, name: str):
        self._fill(self.search_box, name)