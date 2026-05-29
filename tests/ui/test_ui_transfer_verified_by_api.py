import allure
import pytest
from pages.transfer_page import TransferPage
from playwright.sync_api import expect
from config import URL_BAZA_API, URL_BAZA


@pytest.mark.ui
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.auth
@allure.title("UI/API - Transfer funds and verify transaction by API")
@allure.description(
    "Verify that a funds transfer submitted from the UI is reflected in the " \
    "account transactions retrieved by API."
)
@allure.severity("critical")
@allure.epic("UI/API")
@allure.feature("Transfers")
@allure.story("Transfer Funds - UI submission verified by API")
def test_ui_transfer_verified_by_api(playwright, auth_page, transfer_data_load):
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

    # Verific confirmarea transferului in UI
    expect(auth_page.get_by_text("Transfer Complete")).to_be_visible()


    # prin API obtin lista de tranzactii
    request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

    raspuns = request.get(f"{URL_BAZA_API}accounts/{transfer_data_load['from_account']}/transactions", 
                          headers={"Content-Type": "application/json",
                               "Accept": "application/xml"}, data = transfer_data_load)

    # Verific ca raspunsul serverului este OK
    assert raspuns.status == 200    
    r_text = raspuns.text()

    # Verific ca suma transferata este prezenta in raspunsul API
    assert (f"{transfer_data_load['amount']}") in r_text

    request.dispose()