import os
import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.updateprofile_page import UpdateProfilePage
from config import URL_BAZA

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
    # Pagina deja logata
    pagina = auth_context.new_page()
    yield pagina
    pagina.close()

@pytest.fixture
def update_profile_data():
    return {
        "f_name": "John",
        "l_name": "Doe",
        "street": "Str. Scurta 23",
        "city": "Suceava",
        "state": "RO",
        "zip": "720679",
        "phone": "0745123456",
    }

@pytest.fixture
def payment_data_load():
    return {
        "name": "John Payee",
        "address": "Str. Scurta 23",
        "city": "Suceava",
        "state": "RO",
        "zipcode": "720679",
        "phone": "0745123456",
        "account": "123456789",
        "verify_account": "123456789",
        "amount": "10",
        "from_account": "13344",
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # verificăm dacă testul a picat
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")

        #facem screenshot si atasam la raportul Allure
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )