from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    login_page.enter_username("admin")
    login_page.enter_password("admin")
    login_page.click_login()

    home_page.click_new_account()
    home_page.click_update_contact()
    home_page.click_logout()