def test_api_get(playwright):
   request = playwright.request.new_context()
   raspuns = request.get("https://parabank.parasoft.com/parabank/services/bank/customers/12989", 
                         headers={"Accept": "application/json"})

   assert raspuns.status == 200
   date_json = raspuns.json()
   print(date_json)
   assert date_json["id"] == 12989
   request.dispose()