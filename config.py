#URL_BAZA_API = "https://parabank.parasoft.com/parabank/services/bank/"
#URL_BAZA = "https://parabank.parasoft.com/parabank/"

#URL_BAZA = "http://localhost:8080/parabank/"
#URL_BAZA_API = "http://localhost:8080/parabank/services/bank/"

import os

URL_BAZA = os.getenv("URL_BAZA", "http://localhost:8080/parabank/")
URL_BAZA_API = os.getenv("URL_BAZA_API", "http://localhost:8080/parabank/services/bank/")