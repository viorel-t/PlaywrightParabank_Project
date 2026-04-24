import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Test Customer Accounts API")
@allure.description("Verify API for customer account retrieval.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customer Accounts")
@allure.story("Valid customer accounts retrieval")

def test_get_custAccounts(playwright, api_ids_load):
   URL_GET = URL_BAZA_API +  f"customers/{api_ids_load['valid_customer']}/accounts"
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/xml"})

   # Verific statusul raspunsului ca e OK
   assert raspuns.status == 200  

   #Verific daca ID-ul returnat este corect
   xml = raspuns.text()
   assert f"<customerId>{api_ids_load['valid_customer']}</customerId>" in xml

   request.dispose()