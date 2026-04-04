#
# Date pentru formularele din teste
#

import pytest

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
