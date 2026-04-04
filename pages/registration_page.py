from playwright.sync_api import Page, expect

class RegistrationPage:
    def __init__(self, page:Page):
        self.page = page
        self.user_name = page.locator("input[name='customer.firstName']")
        self.user_lastname = page.locator("input[name='customer.lastName']")
        self.user_street = page.locator("input[name='customer.address.street']")
        self.user_city = page.locator("input[name='customer.address.city']")
        self.user_state = page.locator("input[name='customer.address.state']")
        self.user_zipcode = page.locator("input[name='customer.address.zipCode']")
        self.user_phone = page.locator("input[name='customer.phoneNumber']")
        self.user_ssn = page.locator("input[name='customer.ssn']")
        self.user_username = page.locator("input[name='customer.username']")
        self.user_password = page.locator("input[name='customer.password']")
        self.user_repeatedPassword = page.locator("input[name='repeatedPassword']")
        self.register_button = page.get_by_role("button", name="Register")

    def register_form_fill(self, newuser_data):
        self.user_name.fill(newuser_data["first_name"])
        self.user_lastname.fill(newuser_data["last_name"])
        self.user_street.fill(newuser_data["street"])
        self.user_city.fill(newuser_data["city"])
        self.user_state.fill(newuser_data["state"])
        self.user_zipcode.fill(newuser_data["zipcode"])
        self.user_phone.fill(newuser_data["phone_number"])
        self.user_ssn.fill(newuser_data["ssn"])
        self.user_username.fill(newuser_data["username"])
        self.user_password.fill(newuser_data["password"])
        self.user_repeatedPassword.fill(newuser_data["repeated_password"])

    def click_registration(self):
       self.register_button.click()
