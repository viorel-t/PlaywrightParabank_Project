import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

URL_BAZA = "https://parabank.parasoft.com/parabank/"
storage_path = "autentificare/storage_state.json"

@pytest.fixture (scope="session")
def saved_auth_state(browser):
    os.makedirs("autentificare", exist_ok=True)
    
    # Context nou, pentru autentificare
    context = browser.new_context(base_url=URL_BAZA, ignore_https_errors=True)
    pagina = context.new_page()

    pagina_login = LoginPage(pagina)
    pagina_home = HomePage(pagina)
    
    pagina.goto("index.htm")
    pagina_login.login("john", "demo")
    pagina_home.verific_logged_in()
    
    # Salvez starea de autentificare (login-ul a fost reusit)
    context.storage_state(path=storage_path)
    context.close()

@pytest.fixture
def auth_context(browser, saved_auth_state):
    # Context nou, deja autentificat
    context = browser.new_context(storage_state=storage_path, base_url=URL_BAZA, ignore_https_errors=True)
    yield context
    context.close()

@pytest.fixture
def auth_page(auth_context):
    pagina = auth_context.new_page()
    yield pagina
    pagina.close()