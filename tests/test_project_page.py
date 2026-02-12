from pages.project_page import Project      
from playwright.async_api import Page, expect

def test_search_project(page):
    project_page = Project(page)
    project_page.test_select_project_menu()
    project_page.test_search_function("12345")
  