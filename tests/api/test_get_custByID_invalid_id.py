import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Get Customer By Invalid ID - Not Found")
@allure.description("""Verify that the API returns an error response 
                    when requesting a customer with an invalid or non-existent ID.""")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customers")
@allure.story("Get Customer By ID - Invalid ID returns error response")

def test_get_custByID_invalid_id(playwright, api_ids_load):
   URL_GET = URL_BAZA_API + f"customers/{api_ids_load['negative_id']}"
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/json"})

   # Verifc statusul raspunsului pentru un ID invalid
   assert raspuns.status == 400

   # Verific ca raspunsul nu e gol
   assert raspuns.text() is not None 

   #Verific ca mesajul este cel corect (ID invalid)
   assert "Could not find customer" in raspuns.text()

   request.dispose()