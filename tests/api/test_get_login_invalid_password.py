import pytest
import allure
from config import URL_BAZA_API

@pytest.mark.api
@allure.title("Login API - invalid password authentication")
@allure.description("""Verify that the Login API rejects authentication requests with an 
                    invalid password and returns HTTP 400 with the appropriate error message.""")
@allure.severity("critical")
@allure.epic("API")
@allure.feature("Authentication")
@allure.story("Login - Invalid password")

def test_login_custInvalidPass(playwright, api_ids_load):
   URL_GET = (URL_BAZA_API + f"login/{api_ids_load['valid_username']}/password")
   
   request = playwright.request.new_context()
   raspuns = request.get(URL_GET, headers={"Accept": "*/*"})

   # Verific ca raspunsul serverului este 400 Bad Request
   # adica parola este invalida si respinge autentificarea
   assert raspuns.status == 400

   # Verific ca raspunsul contine textul asteptat 
   # care arata eroarea de autentificare
   assert "Invalid username and/or password" in raspuns.text()

   request.dispose()