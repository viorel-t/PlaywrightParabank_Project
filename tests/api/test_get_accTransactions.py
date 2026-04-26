import pytest
import allure
from config import URL_BAZA_API
import xml.etree.ElementTree as ET

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

   # Verific daca raspunsul este in format xml
   assert "xml" in raspuns.headers["content-type"]

   # Extrag lista tranzactiilor din raspuns
   radacina_xml = ET.fromstring(raspuns.text())
   tranzactii = radacina_xml.findall("transaction")

   assert len(tranzactii) > 0
   lista_tranzactii = []
   for tranzactie in tranzactii:
      tranzactie_id = tranzactie.find("id").text
      cont_id = tranzactie.find("accountId").text
      suma = tranzactie.find("amount").text
      descriere_tranzactie = tranzactie.find("description").text

      # Verific daca ID-ul tranzactiei este numeric
      assert tranzactie_id.isdigit()
      
      # Verific daca ID-ul contului returnat este cel pentru care s-a facut request-ul
      assert cont_id == str(api_ids_load['valid_account'])
      
      # Verific ca suma exista si este numar
      assert suma is not None
      valoare_suma = float(suma)
      assert isinstance(valoare_suma, float)

      # Verific ca exista descriere pentru tranzactie
      assert descriere_tranzactie is not None
      
      lista_tranzactii.append(tranzactie_id)
   
   # Verific ca lista de tranzactii nu contine duplicate (sunt tranzactii unice)
   assert len(lista_tranzactii) == len(set(lista_tranzactii))

   request.dispose()