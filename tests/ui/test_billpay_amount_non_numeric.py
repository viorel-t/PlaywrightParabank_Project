import pytest
import allure
from playwright.sync_api import Page, expect
from pages.billpay_page import BillPayPage
from config import URL_BAZA


@pytest.mark.form
@pytest.mark.ui
@allure.title("BillPay with non-numeric amount")
@allure.description("""
Verify that the system validates the amount field and rejects non-numeric input.
Expected results:
- Validation error message is displayed
- Payment is not processed
- No success confirmation is shown
""")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Payment")
@allure.story("BillPay validation")
def test_form_submission(auth_page, payment_data_load, billpay_amount_load):
    payment_page = BillPayPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "billpay.htm")
    
    # Verific daca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Completez câmpurile formularului
    payment_page.payment_form_fill(payment_data_load, billpay_amount_load["nonnumeric_amount"])

    # Efectuez plata
    payment_page.click_send_payment()

    # Verific ca mesajul de eroare este vizibil
    expect(auth_page.locator("#validationModel-amount-invalid")).to_be_visible()
    expect(auth_page.locator("#validationModel-amount-invalid")).to_have_text("Please enter a valid amount.")
    
    # Verific ca mesajul de confirmare nu este vizibil
    assert not auth_page.locator("text=Bill Payment Complete").is_visible()