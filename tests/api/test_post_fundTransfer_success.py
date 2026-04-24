import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Funds Transfer API - successful transfer between accounts")
@allure.description(
    "Verify that a valid funds transfer request between two accounts is processed successfully "
    "and returns a successful response."
)
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Transfers")
@allure.story("Funds Transfer - Successful transaction")

def test_post_fundTransfer(playwright, transfer_data_load):
   URL_POST = (URL_BAZA_API + f"transfer?fromAccountId={transfer_data_load['from_account']}"
                            + f"&toAccountId={transfer_data_load['to_account']}"
                            + f"&amount={transfer_data_load['amount']}")
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = transfer_data_load)
   
   #Verific ca raspunsul este OK
   assert raspuns.status == 200    
   r_text = raspuns.text()

   #Verific daca raspunsul contine "Successfully transfer"
   astept_text = (f"Successfully transferred ${transfer_data_load['amount']} "
                  f"from account #{transfer_data_load['from_account']} "
                  f"to account #{transfer_data_load['to_account']}")
   assert astept_text in r_text
   request.dispose()
