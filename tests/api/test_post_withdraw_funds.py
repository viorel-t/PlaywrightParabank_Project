import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Withdraw funds from account")
@allure.description("""Verify that the withdraw endpoint successfully processes a valid withdrawal request.
Expected results:
- Response status is 200
- Response body confirms the withdrawn amount
- Response body contains the correct account ID""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Accounts")
@allure.story("Withdraw funds")

def test_post_withdrawFunds(playwright, api_ids_load):
   URL_POST = (URL_BAZA_API +  f"withdraw?accountId={api_ids_load['valid_account']}"
              f"&amount={api_ids_load['valid_amount']}")
   
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_ids_load)

   # Verific statusul raspunsului ca e OK
   assert raspuns.status == 200
   raspuns_text = raspuns.text()
   
   # Verific ca request-ul a avut succes si raspunsul contine confirmarea sumei retrase si a contului
   assert "Successfully withdrew" in raspuns_text
   assert f"account #{api_ids_load['valid_account']}" in raspuns_text
   assert f"${api_ids_load['valid_amount']}" in raspuns_text

   request.dispose()