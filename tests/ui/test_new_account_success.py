import pytest
import allure
from pages.new_account_page import OpenAccountPage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Open New Account UI - successful account creation")
@allure.description("""Verify that a logged-in user can successfully create a new bank account 
                    and receives a valid account ID.""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Account Services")
@allure.story("Open New bank Account - Successful creation")
def test_newaacount_submission(auth_page, api_ids_load):
    newaccount_page = OpenAccountPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "openaccount.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Confirm ca sunt in Open Account Page
    expect(auth_page.get_by_role("heading", name="Open New Account")).to_be_visible()

    # Completez formularul de deschidere cont bancar nou
    newaccount_page.fill_newaccount_form(api_ids_load)

    # Trimit formularul - deschid contul
    newaccount_page.click_newaccount()

    # Verific mesajul de confirmare si ca s-a creat un ID pentru contul nou
    expect(auth_page.get_by_role("heading", name="Account Opened!")).to_be_visible()
    expect(auth_page.locator("#rightPanel")).to_contain_text("Congratulations, your account is now open.")
    expect(auth_page.locator("#newAccountId")).not_to_be_empty()