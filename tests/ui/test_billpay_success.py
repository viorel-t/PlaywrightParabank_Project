import pytest
import allure
from playwright.sync_api import Page, expect
from pages.billpay_page import BillPayPage
from config import URL_BAZA


@pytest.mark.form
@pytest.mark.ui
@allure.title("Bill payment with success")
@allure.description("""
Verify that a bill payment can be submitted successfully.
Expected result: payment is completed and confirmation message is displayed.
""")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Payment")
@allure.story("Bill payment - success")
def test_form_submission(auth_page, payment_data_load):
    payment_page = BillPayPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "billpay.htm")
    
    # Verific daca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Completez câmpurile formularului
    payment_page.payment_form_fill(payment_data_load)

    # Efectuez plata
    payment_page.click_send_payment()

    # Verific ca mesajul de confirmare este vizibil
    expect(auth_page.get_by_role("heading", name="Bill Payment Complete")).to_be_visible()

    # Verific suma si mesajul de succes
    expect(auth_page.locator("#rightPanel")).to_contain_text(payment_data_load["amount"])
    expect(auth_page.locator("#rightPanel")).to_contain_text("was successful")