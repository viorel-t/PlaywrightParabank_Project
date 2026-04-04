import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config import URL_BAZA

@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Logout functionality")
@allure.description("""
Verify that a logged-in user can successfully log out from the application.
The test ensures that the user is redirected to the login page,
the session is terminated, and protected pages are no longer accessible.
""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Authentication")
@allure.story("Logout")
def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto(URL_BAZA + "index.htm")
    login_page.login("john", "demo")

    # Verific ca e logat
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

    # Fac Logout
    home_page.click_logout()

    # Verific ca e redirectionat corect
    assert "index.htm" in page.url

    # Verific ca apare login form
    expect(page.locator("input[name='username']")).to_be_visible()

    # Verific ca nu mai e logat
    assert not page.get_by_role("heading", name="Accounts Overview").is_visible()

    # Verific securitatea aplicatiei (accesez pagini protejate dupa logout)
    # iar aplicatia ar trebuie sa refuze accesul.
    page.goto(URL_BAZA + "overview.htm")
    expect(page.locator("input[name='username']")).to_be_visible()