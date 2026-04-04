#
# Test pentru endpoint-ul POST /billpay
#

import pytest
import allure
from config import URL_BAZA_API

URL_POST = URL_BAZA_API + "billpay?accountId=13344&amount=10"

@pytest.mark.api
@allure.title("Test Bill Pay API")
@allure.description("Verify API bill payment.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Bill Pay")
@allure.story("Valid bill payment")
def test_post_billPay(playwright):
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   parametri = {"name": "Test Payee", 
                "address":{"street": "string", "city": "string", "state": "string", "zipCode": "string"}, 
                "phoneNumber": "string"}

   raspuns = request.post(URL_POST, headers={"Content-Type": "application/json",
                               "Accept": "application/xml"}, data = parametri)

   assert raspuns.status == 200    
   xml = raspuns.text()
   
   #Verific daca raspunsul contine tag-ul <billPayResult>
   assert "<billPayResult>" in xml
   request.dispose()