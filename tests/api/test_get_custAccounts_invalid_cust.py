import pytest
import allure
from config import URL_BAZA_API
import xml.etree.ElementTree as ET
from playwright.sync_api import expect

@pytest.mark.api
@allure.title("Accounts API - invalid customer ID")
@allure.description("""Verify that the Accounts API handles requests with 
                    an invalid customer ID and does not return valid account information.""")
@allure.severity("normal")
@allure.epic("API")
@allure.feature("Customer Accounts")
@allure.story("Get Accounts - Invalid customer ID")

def test_get_custAccounts(playwright, api_ids_load):
   URL_GET = URL_BAZA_API +  f"customers/{api_ids_load['invalid_customer']}/accounts"
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/xml"})

   # Verific statusul raspunsului ca e Eroare (nu gaseste clientul)
   assert raspuns.status == 400
   
   # Verific daca raspunsul este in format text (deoarece clientul nu a fost gasit)
   assert "text/plain" in raspuns.headers["content-type"]

   # Verific ca raspunsul e cel asteptat, client inexistent
   assert "Could not find customer" in raspuns.text()

   request.dispose()