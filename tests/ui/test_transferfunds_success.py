import pytest
import allure
from pages.transfer_page import TransferPage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Transfer funds between accounts successfully")
@allure.description("""Verify that a logged-in user can transfer 
                    funds between accounts and receives a success confirmation.""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Account Services")
@allure.story("Transfer Funds - Successful transaction")
def test_form_submission(auth_page, transfer_data_load):
    transfer_funds_page = TransferPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "transfer.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Confirm ca sunt in Transfer Page
    expect(auth_page.get_by_role("heading", name="Transfer Funds")).to_be_visible()

    # Completez formularul de transfer
    transfer_funds_page.fill_transfer_form(transfer_data_load)

    # Trimit formularul - efectuez transferul
    transfer_funds_page.click_transfer()

    # Verific mesajul de confirmare a transferului si ca suma e corecta
    expect(auth_page.get_by_role("heading", name="Transfer Complete!")).to_be_visible()
    expect(auth_page.locator("#rightPanel")).to_contain_text(transfer_data_load["amount"])
    expect(auth_page.locator("#rightPanel")).to_contain_text("has been transferred")