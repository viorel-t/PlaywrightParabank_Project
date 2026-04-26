import pytest
import allure
from config import URL_BAZA_API
import xml.etree.ElementTree as ET

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
   
   # Verific daca raspunsul este in format xml
   assert "xml" in raspuns.headers["content-type"]

   # Extrag lista de conturi din raspuns
   radacina_xml = ET.fromstring(raspuns.text())
   conturi = radacina_xml.findall("account")
   
   assert len(conturi) > 0
   lista_conturi = []
   for cont in conturi:
      cont_id = cont.find("id").text
      client_id = cont.find("customerId").text
      balanta = cont.find("balance").text

      # Verific daca ID-ul contului este numeric
      assert cont_id.isdigit()
      
      # Verific daca ID-ul clientului (customer) returnat este corect
      assert client_id == str(api_ids_load['valid_customer'])
      
      # Verific ca balanta exista si este numar
      assert balanta is not None
      valoare_balanta = float(balanta)
      assert isinstance(valoare_balanta, float)
      
      lista_conturi.append(cont_id)
   
   # Verific ca lista de conturi nu contine duplicate (sunt conturi unice)
   assert len(lista_conturi) == len(set(lista_conturi))

   request.dispose()