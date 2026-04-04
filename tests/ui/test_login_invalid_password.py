import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config import URL_BAZA

@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Login with invalid password")
@allure.description("""
Verify that login fails when a valid username is used with an incorrect password.
Expected result: error message is displayed and user remains on login page.
""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Login")
@allure.story("Invalid login - wrong password")
def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    
    page.goto(URL_BAZA + "index.htm")
    login_page.login("john", "wrong_password")
    
    # Verific ca apare mesaj de eroare
    assert page.locator("text=The username and password could not be verified").is_visible()

    # Verific ca nu sunt redirectionat
    assert "overview" not in page.url.lower()

    # Verific ca nu sunt logat in Home Page
    assert not page.locator("text=Accounts Overview").is_visible()