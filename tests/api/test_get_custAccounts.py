#
# Test pentru endpoint-ul GET /customer accounts by ID
#

import pytest
import allure
from config import URL_BAZA_API

URL_GET = URL_BAZA_API +  "customers/12212/accounts"

@pytest.mark.api
@allure.title("Test Customer Accounts API")
@allure.description("Verify API for customer account retrieval.")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customer Accounts")
@allure.story("Valid customer accounts retrieval")
def test_get_custAccounts(playwright):
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/xml"})

   assert raspuns.status == 200  

   #Verific daca ID-ul returnat este corect
   xml = raspuns.text()
   assert "<customerId>12212</customerId>" in xml

   request.dispose()