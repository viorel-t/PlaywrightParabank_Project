import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Login API - expose credential in URL")
@allure.description("""Verify that the login API uses credentials in URL 
                    wich may represent a security risk.""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Authentication")
@allure.story("Security - Credentials in URL")

def test_get_custByID(playwright, api_ids_load):
   URL_GET = (URL_BAZA_API + f"login/{api_ids_load['valid_username']}/demo")
   
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "application/xml"})

   assert raspuns.status == 200

   # Verific daca raspunsul returnat contine datele 
   # <customer><id><firstName>...<address>...</customer>
   date_xml = raspuns.text()
   assert "<customer>" in date_xml

   request.dispose()