import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Funds Transfer API accepts negative transfer amount")
@allure.description(
    "Verify that the Funds Transfer API processes a transfer request with a negative amount, "
    "highlighting missing validation for invalid transfer values."
)
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Transfers")
@allure.story("Validation - Negative transfer amount")

def test_post_fundTransfer(playwright, transfer_data_load, billpay_amount_load):
   URL_POST = (URL_BAZA_API + f"transfer?fromAccountId={transfer_data_load['from_account']}"
                            + f"&toAccountId={transfer_data_load['to_account']}"
                            + f"&amount={billpay_amount_load['negative_amount']}")
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = transfer_data_load)
   
   # Verific ca raspunsul este neobisnuit/anormal
   assert raspuns.status == 200
   r_text = raspuns.text()

   # Verific daca raspunsul contine comportamentul anormal ("Successfully transferred")
   # valideaza sume negative, ceea ce nu ar trebui sa fie permis
   astept_text = (f"Successfully transferred ${billpay_amount_load['negative_amount']} "
                  f"from account #{transfer_data_load['from_account']} "
                  f"to account #{transfer_data_load['to_account']}")
   assert astept_text in r_text
   request.dispose()
