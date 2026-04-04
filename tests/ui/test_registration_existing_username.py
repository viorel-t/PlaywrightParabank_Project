import pytest
import allure
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from config import URL_BAZA

@pytest.mark.form
@pytest.mark.ui
@allure.title("Registering with existing username")
@allure.description("""
Verify that registering fails when an existing username is used for creating a new account.
Expected result: error message is displayed and user remains on registering page.
""")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Registration")
@allure.story("Invalid registration - existing username")
def test_registration(page: Page, registration_data_existing):
    userregistration_page = RegistrationPage(page)
    page.goto(URL_BAZA + "index.htm")
    
    # Navigare web - click pe "Register" link
    page.click("text=Register")
    
    # Completez formularul de inregistrare
    userregistration_page.register_form_fill(registration_data_existing)

    # Inregistrare user nou
    userregistration_page.click_registration()

    # Verific daca ramin pe aceeasi pagina — nu sunt redirectionat
    assert "register.htm" in page.url

    # Verific daca mesajul de eroare apare
    expect(page.locator('[id="customer.username.errors"]')).to_have_text(
        "This username already exists."
    )