"""
# Date pentru formularele si 
# requesturile din teste
"""
#import time
#from playwright.sync_api import expect
import pytest
#import xml.etree.ElementTree as ET
#from config import URL_BAZA, URL_BAZA_API

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


@pytest.fixture
def api_ids_load():
    return {
        "valid_customer":   12212,
        "valid_username":   "john",
        "invalid_customer": 99999,
        "valid_account":    13344,
        "invalid_account":  99999,
        "negative_id":      -1,
        "zero_id":          0,
        "valid_amount":     10,
        "transaction_amount":     1000,
        "transaction_month":     "april",
        "account_type":     "Debit",
        "account_type_id":     0,   # 0 = CHECKING, 1 = SAVINGS
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

@pytest.fixture
def transaction_data_load():
    return {
        "fromDate": "04-01-2026", # MM-DD-YYYY
        "toDate": "04-27-2026",   # MM-DD-YYYY (05-30-2026)
        "amount": "10",
        "from_account": "13344",
    }