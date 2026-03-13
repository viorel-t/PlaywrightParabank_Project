import pytest
from playwright.sync_api import Page, expect

@pytest.mark.form
@pytest.mark.ui
def test_registration(page: Page) -> None:
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    
    # Click pe "Register" link
    page.click("text=Register")
    
    # Completez formularul de inregistrare
    page.fill("input[name='customer.firstName']", "John")
    page.fill("input[name='customer.lastName']", "Doe")
    page.fill("input[name='customer.address.street']", "Universitatii 123")
    page.fill("input[name='customer.address.city']", "Suceava")
    page.fill("input[name='customer.address.state']", "SV")
    page.fill("input[name='customer.address.zipCode']", "727325")
    page.fill("input[name='customer.phoneNumber']", "555-1234")
    page.fill("input[name='customer.ssn']", "123-45-6789")
    page.fill("input[name='customer.username']", "johndoe")
    page.fill("input[name='customer.password']", "password123")
    page.fill("input[name='repeatedPassword']", "password123")

    # Click pe butonul de inregistrare (Register)
    page.click("input[value='Register']")

    try:
        # Verific mesajul de confirmare
        expect(page.get_by_text("Your account was created successfully.")).to_be_visible()
    except Exception:
        # Dacă mesajul nu este vizibil, verificăm dacă există un mesaj de eroare
        expect(page.get_by_text("Error creating account")).to_be_visible()
        raise AssertionError("Test registration: Eroare la inregistrare.")