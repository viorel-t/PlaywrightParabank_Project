import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Funds Transfer API accepts negative transfer amount")
@allure.description(
    "Verify that the Funds Transfer API returns HTTP 500 Internal Server Error, "
    "when the required amount parameter is missing."
)
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Transfers")
@allure.story("Validation - Missing required (amount) parameter")

def test_post_fundTransfer(playwright, transfer_data_load):
   URL_POST = (URL_BAZA_API + f"transfer?fromAccountId={transfer_data_load['from_account']}"
                            + f"&toAccountId={transfer_data_load['to_account']}")
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = transfer_data_load)
   
   # Verific ca raspunsul este neobisnuit/anormal (500 - internal server error)
   # fata de ce ar trebui sa returneze (400 - bad request /cerere formulata gresit)
   
   assert raspuns.status == 500
   r_text = raspuns.text()

   # Verific daca raspunsul contine comportamentul anormal ("internal error")
   # valideaza sume negative, ceea ce nu ar trebui sa fie permis
   # Eroare pe server/backend --> bug in aplicatie
   
   assert "internal error" in r_text
   
   request.dispose()
