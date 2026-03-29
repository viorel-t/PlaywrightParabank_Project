#
# Test pentru endpoint-ul GET /customer details by ID
#

import pytest
import allure

URL_BAZA = "https://parabank.parasoft.com/parabank/services/bank/customers/12212"

@pytest.mark.api
@allure.title("Test Customer Details API")
@allure.description("Verify API for getting Customer Details.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customer Details")
@allure.story("Valid customer details retrieval")
def test_get_custByID(playwright):
   request = playwright.request.new_context()
   raspuns = request.get(URL_BAZA, headers={"Accept": "application/json"})

   assert raspuns.status == 200

   #Verific daca ID-ul returnat este corect
   date_json = raspuns.json()
   assert date_json["id"] == 12212

   request.dispose()