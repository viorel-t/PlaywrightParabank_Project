import pytest
import allure
from config import URL_BAZA_API
import xml.etree.ElementTree as ET

@pytest.mark.api
@allure.title("Create Account API - successful account creation")
@allure.description("""Verify that a valid API request creates a new bank account 
    for an existing customer and returns a successful response with account details.""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Accounts")
@allure.story("Create account")

def test_post_createAccount(playwright, api_ids_load):
   URL_POST = (URL_BAZA_API +  f"createAccount?customerId={api_ids_load['valid_customer']}"
              f"&newAccountType={api_ids_load['account_type_id']}"
              f"&fromAccountId={api_ids_load['valid_account']}")
   
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_ids_load)

   # Verific statusul raspunsului ca e OK
   assert raspuns.status == 200
   raspuns_xml = raspuns.text()
   root = ET.fromstring(raspuns_xml)
   
   # Verific ca request-ul a creat contul pentru clientul specificat
   assert "<account>" in raspuns_xml
   assert f"{api_ids_load['valid_customer']}" in raspuns_xml
   
   # Verific ca ID-ul returnat este valid
   account_id = root.find(".//id")
   assert account_id is not None
   assert account_id.text is not None

   request.dispose()