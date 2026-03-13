#
# Test pentru endpoint-ul GET /customer accounts by ID
#

import pytest
from utils.utils_saveapi_response import save_api_response

URL_BAZA = "https://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts"

@pytest.mark.api
def test_get_custAccounts(playwright):
   request = playwright.request.new_context()
   raspuns = request.get(URL_BAZA, headers={"Accept": "application/xml"})

   try:
      assert raspuns.status == 200
   except AssertionError:
      #Daca raspunsul serverului nu e 200, salvez raspunsul intr-un fisier text
      path = save_api_response(URL_BAZA, raspuns, "get_custAccounts", "txt", "screenshots")
      raise AssertionError(f"Eroare API Get_custom_accounts. Raspuns salvat in: {path}")
   
   #Verific daca ID-ul returnat este corect
   xml = raspuns.text()
   try:
      assert "<customerId>12212</customerId>" in xml
   except AssertionError:
      raise AssertionError(f"Eroare API Get_custom_accounts. ID (asteptat: 12212), gasit: {xml.find('<customerId>')}")
   
   request.dispose()