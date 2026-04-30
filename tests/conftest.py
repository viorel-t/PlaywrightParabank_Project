"""
# Date pentru formularele si 
# requesturile din teste
"""

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

    username = "john"
    password = "demo"

    login = request.get(f"{URL_BAZA_API}login/{username}/{password}",
                        headers={"Accept": "application/xml"})
    if login.status != 200:
        register_response = request.post(
            f"{URL_BAZA}register.htm",
            form={
                "customer.firstName": "Test",
                "customer.lastName": "User",
                "customer.address.street": "Test Street",
                "customer.address.city": "Test City",
                "customer.address.state": "TS",
                "customer.address.zipCode": "12345",
                "customer.phoneNumber": "1234567890",
                "customer.ssn": "123456789",
                "customer.username": username,
                "customer.password": password,
                "repeatedPassword": password,
            },
        )
        print(register_response.text())
        assert register_response.status in [200, 302]

    login_response = request.get(
        f"{URL_BAZA_API}login/{username}/{password}",
        headers={"Accept": "application/xml"}
    )

    assert login_response.status == 200

    root = ET.fromstring(login_response.text())
    customer_id = root.findtext("id")

    assert customer_id is not None

    accounts_response = request.get(
        f"{URL_BAZA_API}customers/{customer_id}/accounts",
        headers={"Accept": "application/xml"}
    )

    assert accounts_response.status == 200

    accounts_root = ET.fromstring(accounts_response.text())
    accounts = accounts_root.findall("account")

    assert len(accounts) >= 2

    valid_account = accounts[0].findtext("id")
    to_account = accounts[1].findtext("id")

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