from playwright.sync_api import Page, expect

class BillPayPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.customer_name = page.locator('input[name="payee.name"]')
        self.customer_streetaddress = page.locator('input[name="payee.address.street"]')
        self.customer_cityaddress = page.locator('input[name="payee.address.city"]')
        self.customer_stateaddress = page.locator('input[name="payee.address.state"]')
        self.customer_zipcode = page.locator('input[name="payee.address.zipCode"]')
        self.customer_phone = page.locator('input[name="payee.phoneNumber"]')
        self.customer_account = page.locator('input[name="payee.accountNumber"]')
        self.customer_verify_account = page.locator('input[name="verifyAccount"]')
        self.customer_amount = page.locator('input[name="amount"]')
        self.customer_from_account = page.locator('select[name="fromAccountId"]')
        self.send_payment_button = page.get_by_role("button", name="Send Payment")

    def click_send_payment(self):
        self.send_payment_button.click()

    def payment_form_fill(self, date_payment, amount=None):
        final_amount = amount if amount is not None else date_payment["amount"]
        self.customer_name.fill(date_payment["name"])
        self.customer_streetaddress.fill(date_payment["address"])
        self.customer_cityaddress.fill(date_payment["city"])
        self.customer_stateaddress.fill(date_payment["state"])
        self.customer_zipcode.fill(date_payment["zipcode"])
        self.customer_phone.fill(date_payment["phone"])
        self.customer_account.fill(date_payment["account"])
        self.customer_verify_account.fill(date_payment["verify_account"])
        self.customer_amount.fill(str(final_amount))
        self.customer_from_account.select_option(date_payment["from_account"])
