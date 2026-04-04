import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config import URL_BAZA

@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Login with valid credentials")
@allure.description("""
Verify that a registered user can successfully log in using valid credentials.
The test ensures that the user is redirected to the Accounts Overview page
and that no error message is displayed.
""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Authentication")
@allure.story("Successful login")
def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto(URL_BAZA + "index.htm")
    login_page.login("john", "demo")
   
    # Verific ca e redirectionat corect
    assert "overview" in page.url.lower()

    # Confirm ca sunt in Home Page (Accounts Overview) - UI corect dupa login
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()
    
    # Verific ca nu sunt erori
    assert not page.locator("text=The username and password could not be verified").is_visible()

    # Verific ca tabelul este vizibil / datele sunt afisate
    expect(page.locator("table")).to_be_visible()

    # Verific buton Log-out (vizibil); sesiune activa
    expect(home_page.logout_link).to_be_visible()
    home_page.click_logout()