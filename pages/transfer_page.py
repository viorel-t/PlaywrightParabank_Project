from playwright.sync_api import Page, expect

class TransferPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.transfer_amount = page.locator('input[id="amount"]')
        self.transfer_from_account = page.locator('select[id="fromAccountId"]')
        self.transfer_to_account = page.locator('select[id="toAccountId"]')
        self.transfer_button = page.get_by_role("button", name="Transfer")

    def click_transfer(self):
        self.transfer_button.click()

    def fill_transfer_form(self, transfer_date):
        self.transfer_from_account.select_option(value=transfer_date["from_account"])
        self.transfer_to_account.select_option(value=transfer_date["to_account"])
        self.transfer_amount.fill(transfer_date["amount"])
