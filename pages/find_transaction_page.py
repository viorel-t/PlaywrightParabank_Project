from playwright.sync_api import Page, expect

class FindTransactionPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.transaction_account_id = page.locator('select[id="accountId"]')
        
        #self.transaction_id = page.locator('input[id="transactionId"]')
        #self.transaction_button_byId = page.locator('button[id="findById"]')
        
        self.transaction_date = page.locator('input[id="transactionDate"]')
        self.transaction_button_byDate = page.locator('button[id="findByDate"]')
        
        self.transaction_fromdate = page.locator('input[id="fromDate"]')
        self.transaction_todate = page.locator('input[id="toDate"]')
        self.transaction_button_byDateRange = page.locator('button[id="findByDateRange"]')
        
        self.transaction_amount = page.locator('input[id="amount"]')
        self.transaction_button_byAmount = page.locator('button[id="findByAmount"]')

    def click_transaction_byDate(self):
        self.transaction_button_byDate.click()

    def fill_transaction_form_byDate(self, transfer_date):
        self.transaction_account_id.select_option(value=transfer_date["from_account"])
        self.transaction_date.fill(transfer_date["toDate"])

    def click_transaction_byDateRange(self):
        self.transaction_button_byDateRange.click()

    def fill_transaction_form_byDateRange(self, transfer_date):
        self.transaction_account_id.select_option(value=transfer_date["from_account"])
        self.transaction_fromdate.fill(transfer_date["fromDate"])
        self.transaction_todate.fill(transfer_date["toDate"])

    def click_transaction_byAmount(self):
        self.transaction_button_byAmount.click()

    def fill_transaction_form_byAmount(self, transfer_date):
        self.transaction_account_id.select_option(value=transfer_date["from_account"])
        self.transaction_amount.fill(transfer_date["amount"])
