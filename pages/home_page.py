from playwright.sync_api import Page, expect

class HomePage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.newaccount_link = page.get_by_role("link", name="Open New Account")
        self.accountoverview_link = page.get_by_role("link", name="Account Overview")
        self.transferfunds_link = page.get_by_role("link", name="Transfer Funds")
        self.billpay_link = page.get_by_role("link", name="Bill Pay")
        self.findtransactions_link = page.get_by_role("link", name="Find Transactions")
        self.updatecontact_link = page.get_by_role("link", name="Update Contact Info")
        self.requestloan_link = page.get_by_role("link", name="Request Loan")
        self.logout_link = page.get_by_role("link", name="Log Out")

    def verific_logged_in(self):
        expect(self.logout_link).to_be_visible()

    def click_new_account(self):
        self.newaccount_link.click()

    def click_account_overview(self):
        self.accountoverview_link.click()

    def click_transfer_funds(self):
        self.transferfunds_link.click()

    def click_bill_pay(self):
        self.billpay_link.click()

    def click_find_transactions(self):
        self.findtransactions_link.click()

    def click_update_contact(self):
        self.updatecontact_link.click()

    def click_request_loan(self):
        self.requestloan_link.click()

    def click_logout(self):
        self.logout_link.click()
