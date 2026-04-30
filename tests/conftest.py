"""
# Date pentru formularele si 
# requesturile din teste
"""
import time
from playwright.sync_api import expect
import pytest
import xml.etree.ElementTree as ET
from config import URL_BAZA, URL_BAZA_API

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

@pytest.fixture
def registration_data_new():
    return {
        "first_name": "John Test",
        "last_name": "Newdoe",
        "street": "Str. Scurta 123",
        "city": "Suceava",
        "state": "RO",
        "zipcode": "720679",
        "phone_number": "0745123456",
        "ssn": "123456789",
        "username": "usertest",
        "password": "test",
        "repeated_password": "test",
    }

@pytest.fixture
def registration_data_existing():
    return {
        "first_name": "John Two",
        "last_name": "Newdoe",
        "street": "Str. Scurta 123",
        "city": "Suceava",
        "state": "RO",
        "zipcode": "720679",
        "phone_number": "0745123456",
        "ssn": "123456789",
        "username": "usertest",
        "password": "test",
        "repeated_password": "test",
    }

@pytest.fixture
def transfer_data_load():
    return {
        "amount": "10",
        "from_account": "13344",
        "to_account": "12900",
    }


#@pytest.fixture
#def api_ids_load():
#    return {
#        "valid_customer":   12212,
#        "invalid_customer": 99999,
#        "valid_account":    13344,
#        "invalid_account":  99999,
#        "negative_id":      -1,
#        "zero_id":          0,
#        "valid_amount":     10,
#        "transaction_amount":     1000,
#        "transaction_month":     "april",
#        "account_type":     "Debit",
#   }

@pytest.fixture(scope="session")
def api_ids_load(playwright):
    request = playwright.request.new_context()

    #username = "johnydoe"
    #password = "demo"
    username = f"ci_user_{int(time.time())}"
    password = "Test123!"

    login = request.get(f"{URL_BAZA_API}login/{username}/{password}",
                        headers={"Accept": "application/xml"})
    if login.status != 200:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(f"{URL_BAZA}register.htm")

        page.fill("input[name='customer.firstName']", "Test")
        page.fill("input[name='customer.lastName']", "User")
        page.fill("input[name='customer.address.street']", "Test Street")
        page.fill("input[name='customer.address.city']", "Test City")
        page.fill("input[name='customer.address.state']", "TS")
        page.fill("input[name='customer.address.zipCode']", "12345")
        page.fill("input[name='customer.phoneNumber']", "1234567890")
        page.fill("input[name='customer.ssn']", "123-45-6789")
        page.fill("input[name='customer.username']", username)
        page.fill("input[name='customer.password']", password)
        page.fill("input[name='repeatedPassword']", password)

        page.get_by_role("button", name="Register").click()

        print(page.content())
        print("URL:", page.url)
        if page.locator("p.error").is_visible():
            print("ERROR TEXT:", page.locator("p.error").inner_text())
        expect(page.locator("h1.title")).to_contain_text(f"Welcome {username}")
        expect(page.get_by_text("Your account was created successfully.")).to_be_visible()

        browser.close()

    login_response = request.get(
        f"{URL_BAZA_API}login/{username}/{password}",
        headers={"Accept": "application/xml"}
    )

    # verific daca am login reusit
    assert login_response.status == 200
    
    ## obtin id-ul userului logat
    root = ET.fromstring(login_response.text())
    customer_id = root.findtext("id")

    assert customer_id is not None

    # obtin primul cont al userului
    accounts_response = request.get(
        f"{URL_BAZA_API}customers/{customer_id}/accounts",
        headers={"Accept": "application/xml"}
    )

    assert accounts_response.status == 200

    accounts_root = ET.fromstring(accounts_response.text())
    accounts = accounts_root.findall("account")

    assert len(accounts) >= 1

    valid_account = accounts[0].findtext("id")
    #to_account = accounts[1].findtext("id")

   # creez al doilea cont
    second_account_response = request.post(
        f"{URL_BAZA_API}createAccount",
        params={
            "customerId": customer_id,
            "newAccountType": 0,      # 0 = CHECKING, 1 = SAVINGS
            "fromAccountId": valid_account
        },
        headers={"Accept": "application/xml"}
    )

    assert second_account_response.status == 200

    # obtin id-ul celui de-al doilea cont
    root = ET.fromstring(second_account_response.text())
    to_account = root.findtext("id")
    
    # verific daca al doilea cont este nevid si numeric
    assert to_account is not None
    assert to_account.isdigit()

    request.dispose()

    return {
        "valid_customer": customer_id,
        "invalid_customer": 99999,
        "valid_account": valid_account,
        "invalid_account": 99999,
        "negative_id": -1,
        "zero_id": 0,
        "valid_amount": 10,
        "to_account": to_account,
        "transaction_amount": 1000,
        "transaction_month": "april",
        "account_type": "Debit",
    }

@pytest.fixture
def api_billpay_data_load():
    return {
        "name": "apiTest Payee",
        "address": {
            "street":  "apiStreet",
            "city":    "apiCity",
            "state":   "apiState",
            "zipCode": "apiZip"
        },
        "phoneNumber": "apiPhone",
    }

@pytest.fixture(params=
[
    (
        "accountId",
        "",
        "15", # amount
        {
            "name":          "Test Payee",
            "address":       {"street": "123 Main St", 
                              "city": "Springfield", 
                              "state": "IL", 
                              "zipCode": "62701"},
            "phoneNumber":   "555-1234",
            "accountNumber": "13344"
        }
    ),
    (
        "amount",
        "13344", # accountId
        "",
        {
            "name":          "Test Payee",
            "address":       {"street": "123 Main St", 
                              "city": "Springfield", 
                              "state": "IL", 
                              "zipCode": "62701"},
            "phoneNumber":   "555-1234",
            "accountNumber": "13344"
        }
    ),
])
def missing_field_payload(request):
    # returneaza tuple (missing_field, account, amount, payload)
    return request.param

@pytest.fixture
def transfer_sameaccount_load():
    return {
        "amount": "10",
        "from_account": "12345",
        "to_account": "12345",
    }

@pytest.fixture
def request_loan_load():
    return {
        "loan_amount": "100",
        "down_payment": "100",
        "from_account": "12345",
    }

@pytest.fixture
def billpay_amount_load():
    return {
        "zero_amount": "0",
        "negative_amount": "-100",
        "nonnumeric_amount": "text",
        "empty_amount": "",
    }

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