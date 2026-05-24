import pytest
import allure
from pages.find_transaction_page import FindTransactionPage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Find Transactions UI - search transactions by amount")
@allure.description("""Verify that a logged-in user can successfully search account transactions  
                    by amount and matching transactions are displayed in the results table.""")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Account Services")
@allure.story("Find Transactions - Search by amount")
def test_form_submission(auth_page, transaction_data_load):
    transaction_page = FindTransactionPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "findtrans.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Confirm ca sunt in Find Transaction Page
    expect(auth_page.get_by_role("heading", name="Find Transactions")).to_be_visible()

    # Completez formularul de cautare dupa Amount
    transaction_page.fill_transaction_form_byAmount(transaction_data_load)

    # Trimit formularul - efectuez cautarea dupa Amount
    transaction_page.click_transaction_byAmount()

    # Verific ca exista un rezultat si ca tabelul cu rezultate este vizibil
    # si contine amount-ul specificat
    expect(auth_page.get_by_role("heading", name="Transaction Results")).to_be_visible()
    expect(auth_page.locator("#transactionTable")).to_be_visible()
    assert transaction_data_load["amount"] in auth_page.locator("#transactionTable").text_content()

