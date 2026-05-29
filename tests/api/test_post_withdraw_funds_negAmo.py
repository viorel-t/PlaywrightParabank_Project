import pytest
import allure
from config import URL_BAZA_API
import re

@pytest.mark.api
@allure.title("Withdraw API accepts negative withdrawal amount")
@allure.description("""Verify that the Withdraw API processes withdraw requests with a negative 
                    amount, highlighting missing validation for invalid transaction values.""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Withdraw")
@allure.story("Validation - Negative withdrawal amount")

def test_post_withdraw_negativeAmount(playwright, api_ids_load, billpay_amount_load):
   URL_POST = (URL_BAZA_API +  f"withdraw?accountId={api_ids_load['valid_account']}"
              f"&amount={billpay_amount_load['negative_amount']}")
   
   request = playwright.request.new_context(storage_state="autentificare/storage_state.json")
   
   balanta_raspuns_before = request.get(f"{URL_BAZA_API}accounts/{api_ids_load['valid_account']}")
   balanta_before = extrag_balanta(balanta_raspuns_before.text())
   
   raspuns = request.post(URL_POST, headers={
                              "Content-Type": "application/json",
                               "Accept": "application/xml"}, 
                               data = api_ids_load)

   # Verific statusul raspunsului pentru comportament neasteptat
   assert raspuns.status == 200
   raspuns_text = raspuns.text()
   
   # Verific ca request-ul a avut succes si raspunsul contine confirmarea sumei retrase si a contului
   # aplicatia accepta retrageri negative (corupere balanta, depunere mascata, bypass validare)
   # validation/security flow
   assert "Successfully withdrew" in raspuns_text
   assert f"${billpay_amount_load['negative_amount']}" in raspuns_text
   assert f"from account #{api_ids_load['valid_account']}" in raspuns_text

   balanta_raspuns_after = request.get(f"{URL_BAZA_API}accounts/{api_ids_load['valid_account']}")
   balanta_after = extrag_balanta(balanta_raspuns_after.text())

   # Comportamentul incorect: balanta creste dupa retragere negativa
   assert balanta_after > balanta_before
   
   # Printeaza in output valorile (-s pentru rulare)
   #print("\nBalance before:", balanta_before)
   #print("\nBalance after:", balanta_after)

   request.dispose()


def extrag_balanta(xml_text):
    gasit = re.search(r"<balance>(.*?)</balance>", xml_text)
    assert gasit is not None
    return float(gasit.group(1))