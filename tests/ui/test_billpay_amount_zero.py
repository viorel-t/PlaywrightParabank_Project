import pytest
import allure
from playwright.sync_api import Page, expect
from pages.billpay_page import BillPayPage
from config import URL_BAZA


@pytest.mark.form
@pytest.mark.ui
@allure.title("Bill pay with zero amount")
@allure.description("""
Verify that the system does not allow bill payment with an amount of 0.
Expected results:
- Payment is not processed
- No success confirmation is displayed
- Application may display an error or reject the request
""")
@allure.severity("critical")
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
    payment_page.payment_form_fill(payment_data_load, billpay_amount_load["zero_amount"])

    # Efectuez plata
    payment_page.click_send_payment()

    # Verific ca mesajul de eroare este vizibil
    expect(auth_page.get_by_role("heading", name="Error!")).to_be_visible()
    
    # Verific ca mesajul de confirmare nu este vizibil
    assert not auth_page.locator("text=Bill Payment Complete").is_visible()