import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config import URL_BAZA

@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Session persistance after page refresh")
@allure.description(""" Verify that a logged-in user remains authenticated after refreshing the page.
Expected results: - User stays on an authenticated page after refresh; - Accounts Overview is still 
                    visible; - Login form is not displayed
""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Authentication")
@allure.story("Session persistence")
def test_login(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto(URL_BAZA + "index.htm")
    login_page.login("john", "demo")
    
    # Verific ca userul este logat si URL-ul este corect
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()
    assert "overview.htm" in page.url
    
    # Refresul paginii
    page.reload()
    
    # Verific ca userul a ramas logat dupa refresh
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()
    
    # Verific ca sesiunea e activa (nu apare login form)
    expect(page.locator("text=Log Out")).to_be_visible()
    expect(page.locator("input[name='username']")).not_to_be_visible()
    home_page.click_logout()