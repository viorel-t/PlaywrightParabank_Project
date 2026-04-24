from playwright.sync_api import Page, expect

class RequestLoanPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.loan_amount = page.locator('input[id="amount"]')
        self.down_payment = page.locator('input[id="downPayment"]')
        self.loan_from_account = page.locator('select[id="fromAccountId"]')
        self.loan_button = page.get_by_role("button", name="Apply Now")

    def click_requestloan(self):
        self.loan_button.click()

    def fill_loan_form(self, transfer_date):
        self.loan_amount.fill(transfer_date["loan_amount"])
        self.down_payment.fill(transfer_date["down_payment"])
        self.loan_from_account.select_option(value=transfer_date["from_account"])
