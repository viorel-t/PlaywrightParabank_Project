import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Test Customer Details API")
@allure.description("Verify API for getting Customer Details.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customer Details")
@allure.story("Valid customer details retrieval")

def test_get_custByID(playwright, api_ids_load):
   URL_GET = (URL_BAZA_API + f"customers/{api_ids_load['valid_customer']}")
   
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/json"})

   assert raspuns.status == 200

   #Verific daca ID-ul returnat este corect
   date_json = raspuns.json()
   assert date_json["id"] == api_ids_load['valid_customer']

   request.dispose()