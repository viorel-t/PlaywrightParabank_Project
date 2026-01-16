def test_api_post(playwright):
   request = playwright.request.new_context()
   parametri = {"name": "Test Payee", 
                "address":{"street": "string", "city": "string", "state": "string", "zipCode": "string"}, 
                "phoneNumber": "string"}
   raspuns = request.post("https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=13344&amount=20", 
                         headers={
                            "Content-Type": "application/json",
                            "Accept": "application/xml"}, data = parametri)

   assert raspuns.status == 200
   #date_json = raspuns.json()
   #print(date_json)
   xml = raspuns.text()
   print(xml)
   assert "<billPayResult>" in xml
   request.dispose()