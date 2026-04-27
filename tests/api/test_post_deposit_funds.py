import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Deposit funds in account")
@allure.description("""Verify that the API endpoint successfully processes a valid deposit request.
Expected results:
- Response status is 200
- Response body confirms the deposited amount
- Response body contains the correct account ID""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Accounts")
@allure.story("Deposit funds")

def test_post_depositFunds(playwright, api_ids_load):
   URL_POST = (URL_BAZA_API +  f"deposit?accountId={api_ids_load['valid_account']}"
              f"&amount={api_ids_load['valid_amount']}")
   
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_ids_load)

   # Verific statusul raspunsului ca e OK
   assert raspuns.status == 200
   raspuns_text = raspuns.text()
   
   # Verific ca request-ul a avut succes si raspunsul contine confirmarea sumei depuse si a contului
   assert "Successfully deposited" in raspuns_text
   assert f"${api_ids_load['valid_amount']}" in raspuns_text
   assert f"account #{api_ids_load['valid_account']}" in raspuns_text

   request.dispose()