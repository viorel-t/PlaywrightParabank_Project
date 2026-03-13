#
# Test pentru endpoint-ul POST /billpay
#

import pytest
from utils.utils_saveapi_response import save_api_response

URL_BAZA = "https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=13344&amount=10"

@pytest.mark.api
def test_post_billPay(playwright):
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   parametri = {"name": "Test Payee", 
                "address":{"street": "string", "city": "string", "state": "string", "zipCode": "string"}, 
                "phoneNumber": "string"}

   raspuns = request.post(URL_BAZA, headers={"Content-Type": "application/json",
                               "Accept": "application/xml"}, data = parametri)

   try:
      assert raspuns.status == 200
   except AssertionError:
      #Daca raspunsul serverului nu e 200, salvez raspunsul intr-un fisier
      path = save_api_response("", raspuns, "post_billpay", "html", "screenshots")
      raise AssertionError(f"Eroare POST billPay. Raspuns salvat in: {path}")

   xml = raspuns.text()

   #Verific daca raspunsul contine tag-ul <billPayResult>
   try:
      assert "<billPayResult>" in xml
   except AssertionError:
      raise AssertionError(f"Raspunsul API POST billPay nu contine tag-ul <billPayResult>.")

   request.dispose()