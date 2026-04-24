import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Test Bill Pay API")
@allure.description("Verify API bill payment.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Bill Pay")
@allure.story("Valid bill payment")

def test_post_billPay(playwright, api_ids_load, api_billpay_data_load):
   URL_POST = (URL_BAZA_API + f"billpay?accountId={api_ids_load['valid_account']}"
                              f"&amount={api_ids_load['valid_amount']}")
   
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")

   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_billpay_data_load)
   
   assert raspuns.status == 200    
   xml = raspuns.text()
      
   #Verific daca raspunsul contine tag-ul <billPayResult>
   assert "<billPayResult>" in xml
   request.dispose()