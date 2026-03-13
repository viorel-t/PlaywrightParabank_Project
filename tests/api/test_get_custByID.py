#
# Test pentru endpoint-ul GET /customer details by ID
#

import pytest
from utils.utils_saveapi_response import save_api_response

URL_BAZA = "https://parabank.parasoft.com/parabank/services/bank/customers/12212"

@pytest.mark.api
def test_get_custByID(playwright):
   request = playwright.request.new_context()
   raspuns = request.get(URL_BAZA, headers={"Accept": "application/json"})

   try:
      assert raspuns.status == 200
   except AssertionError:
      #Daca raspunsul serverului nu e 200, salvez raspunsul intr-un fisier text
      path = save_api_response(URL_BAZA, raspuns, "get_custByID", "txt", "screenshots")
      raise AssertionError(f"Eroare API Get_custom_byID. Raspuns salvat in: {path}")
   
   #Verific daca ID-ul returnat este corect
   date_json = raspuns.json()
   try:
      assert date_json["id"] == 12212
   except AssertionError:
      raise AssertionError(f"Eroare API Get_custom_byID. ID (asteptat: 12212), gasit: {date_json['id']}")
   
   request.dispose()