import pytest
import allure
from pages.transfer_page import TransferPage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Transfer funds to the same account")
@allure.description("""Verify the application behavior when transferring funds to the same account.
Expected result: the transfer is processed successfully and a confirmation message is displayed,
EVEN when the SOURCE and DESTINATION account are IDENTICAL.""")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Transfer Funds")
@allure.story("Transfer to the same account")
def test_form_submission(auth_page, transfer_sameaccount_load):
    transfer_funds_page = TransferPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "transfer.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Confirm ca sunt in Transfer Page
    expect(auth_page.get_by_role("heading", name="Transfer Funds")).to_be_visible()

    # Completez formularul de transfer
    transfer_funds_page.fill_transfer_form(transfer_sameaccount_load)

    # Trimit formularul - efectuez transferul
    transfer_funds_page.click_transfer()

    # Verific mesajul de confirmare a transferului si ca suma e corecta
    # si conturile sursa si destinatie sunt identice
    expect(auth_page.get_by_role("heading", name="Transfer Complete!")).to_be_visible()
    expect(auth_page.locator("#rightPanel")).to_contain_text("has been transferred")
    expect(auth_page.locator("#amountResult")).to_have_text("$" + transfer_sameaccount_load["amount"] + ".00")
    expect(auth_page.locator("#fromAccountIdResult")).to_have_text(transfer_sameaccount_load["from_account"])
    expect(auth_page.locator("#toAccountIdResult")).to_have_text(transfer_sameaccount_load["to_account"])