import pytest
import allure
from config import URL_BAZA_API
import xml.etree.ElementTree as ET
from datetime import datetime

@pytest.mark.api
@allure.title("Account transactions filtered by month and account type")
@allure.description("""Verify that the API correctly returns transactions 
                    filtered by a specific month for a given type account.

Expected results:
- Response status is 200 (OK)
- Response content type is XML
- At least one transaction is returned
- Each transaction:
  - has a numeric ID
  - belongs to the requested account
  - has a valid numeric amount
  - matches the requested month
  - contains a non-empty description
  - matches the requested account type                    
- All transaction IDs are unique""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Transactions")
@allure.story("Filter transactions by month and account type")

def test_get_accountTransactions(playwright, api_ids_load):
   URL_GET = (URL_BAZA_API +  f"accounts/{api_ids_load['valid_account']}/transactions/"
              f"month/{api_ids_load['transaction_month']}/"
              f"type/{api_ids_load['account_type']}")
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
      tip_cont = tranzactie.find("type").text
      suma = tranzactie.find("amount").text
      data_tranzactie = tranzactie.find("date").text
      descriere_tranzactie = tranzactie.find("description").text

      # Verific daca ID-ul tranzactiei este numeric
      assert tranzactie_id.isdigit()
      
      # Verific daca ID-ul contului returnat este cel pentru care s-a facut request-ul
      assert cont_id == str(api_ids_load['valid_account'])

      # Verific daca tipul contului returnat este cel pentru care s-a facut request-ul
      assert tip_cont == str(api_ids_load['account_type'])

      # Verific ca suma exista si este numar
      assert suma is not None
      valoare_suma = float(suma)
      assert isinstance(valoare_suma, float)

      # Extrag data tranzactiei din raspuns
      data_request = int(data_tranzactie[5:7])
      
      # Transform data cautata (data_numar) in numar
      data_numar = datetime.strptime(api_ids_load['transaction_month'], "%B").month
      
      # Verific ca luna tranzactiilor este cea cautata
      assert data_request == data_numar

      # Verific ca exista descriere pentru tranzactie
      assert descriere_tranzactie is not None
      
      lista_tranzactii.append(tranzactie_id)
   
   # Verific ca lista de tranzactii nu contine duplicate (sunt tranzactii unice)
   assert len(lista_tranzactii) == len(set(lista_tranzactii))

   request.dispose()