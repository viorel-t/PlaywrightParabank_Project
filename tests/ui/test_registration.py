import pytest
import allure
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from config import URL_BAZA

@pytest.mark.form
@pytest.mark.ui
@allure.title("Test Registration")
@allure.description("Verify user can register successfully.")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Registration")
@allure.story("Valid user registration")
def test_registration(page: Page, registration_data_new):
    userregistration_page = RegistrationPage(page)
    page.goto(URL_BAZA + "index.htm")
    
    # Navigare web - click pe "Register" link
    page.click("text=Register")
    
    # Completez formularul de inregistrare
    userregistration_page.register_form_fill(registration_data_new)

    # Inregistrare user nou
    userregistration_page.click_registration()

    # Verific daca mesajul de confirmare este vizibil si contul a fost creat cu succes
    expect(page.get_by_role("heading", name="Welcome " + registration_data_new["username"])).to_be_visible()
    expect(page.get_by_text("Your account was created successfully.")).to_be_visible()
    
    # Verific daca userul este logat dupa inregistrare
    expect(page.get_by_role("link", name="Log Out")).to_be_visible()
    expect(page.locator("#rightPanel")).to_contain_text("You are now logged in")
