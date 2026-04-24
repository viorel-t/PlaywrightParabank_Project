import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Bill Pay API - request with missing required fields")
@allure.description(
    "Verify that the Bill Pay API handles requests with missing required fields "
    "and returns an appropriate error response."
)
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Bill Payment")
@allure.story("Bill Pay - Missing required fields")

def test_post_billPay_missing_rf(playwright, missing_field_payload):
   missing_field, valid_account, valid_amount, payload = missing_field_payload
   
   URL_POST = URL_BAZA_API + f"billpay?accountId={valid_account}&amount={valid_amount}"
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = payload
   )

   # Verific ca statusul raspunsului sa indice o eroare
   assert raspuns.status in [400, 500]
   request.dispose()