import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Test  Account History API")
@allure.description("""Verify that the account transactions endpoint returns a valid XML response
for a given account ID.""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Customer Accounts")
@allure.story("Get account transactions")

def test_get_accountTransactions(playwright, api_ids_load):
   URL_GET = URL_BAZA_API +  f"accounts/{api_ids_load['valid_account']}/transactions"
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/xml"})

   # Verific statusul raspunsului ca e OK
   assert raspuns.status == 200  

   # Verific daca ID-ul returnat este corect
   xml = raspuns.text()
   assert f"<accountId>{api_ids_load['valid_account']}</accountId>" in xml
   
   # Exista o descriere pentru tranzactie
   assert "<description>" in xml
   request.dispose()