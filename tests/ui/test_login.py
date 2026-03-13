import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.ui
def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    login_page.login("john", "demo")
    home_page.verific_logged_in()
    home_page.click_logout()