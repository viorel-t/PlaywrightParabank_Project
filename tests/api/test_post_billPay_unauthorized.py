import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Bill payment without authentication")
@allure.description("""Verify that the bill payment endpoint rejects requests made without 
                    authentication. Expected results: - request rejected; - error status returned;
                    - payment isn't processed""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Bill Payment")
@allure.story("Unauthorized bill payment")

def test_post_billPay_unauthorized(playwright, missing_field_payload):
   missing_field, valid_account, valid_amount, payload = missing_field_payload
   
   URL_POST = URL_BAZA_API + f"billpay?accountId={valid_account}&amount={valid_amount}"
   request = playwright.request.new_context()

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = payload
   )

   # Verific ca statusul raspunsului sa indice o eroare
   assert raspuns.status in [400, 401, 403, 500]
   request.dispose()