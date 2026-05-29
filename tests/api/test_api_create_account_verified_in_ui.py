import allure
import pytest
import re
from playwright.sync_api import expect
from config import URL_BAZA_API


@pytest.mark.ui
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.auth
@allure.title("API/UI - Create account by API and verify in UI")
@allure.description(
    """Verify that a new account created through the API is displayed in 
    the Accounts Overview page.""")
@allure.severity("critical")
@allure.epic("UI/API")
@allure.feature("Accounts")
@allure.story("Create Account - API creation verified in UI")
def test_api_create_account_verified_in_ui(auth_page, playwright, api_ids_load):
    URL_POST = (URL_BAZA_API +  f"createAccount?customerId={api_ids_load['valid_customer']}"
              f"&newAccountType={api_ids_load['account_type_id']}"
              f"&fromAccountId={api_ids_load['valid_account']}")

    # Creez cont nou prin API
    request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
    raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_ids_load)
    
    # Verific raspunsul serverului ca e OK
    assert raspuns.status == 200
    raspuns_xml = raspuns.text()

    # Extrag ID-ul contului nou creat
    gasesc_id = re.search(r"<id>(\d+)</id>", raspuns_xml)
    assert gasesc_id is not None
    cont_nou_id = gasesc_id.group(1)
    
    # Verific prin UI ca noul cont este vizibil in Accounts Overview
    auth_page.goto("overview.htm")
    expect(auth_page.get_by_role("link", name=cont_nou_id)).to_be_visible()

    request.dispose()