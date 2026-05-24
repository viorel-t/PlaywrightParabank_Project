from playwright.sync_api import Page, expect

class OpenAccountPage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.newaccount_type = page.locator('select[id="type"]')
        self.newaccount_amount_from_account = page.locator('select[id="fromAccountId"]')
        self.newaccount_button = page.get_by_role("button", name="Open New Account")

    def click_newaccount(self):
        self.newaccount_button.click()

    def fill_newaccount_form(self, cont_date):
        self.newaccount_type.select_option(value=str(cont_date["account_type_id"]))
        self.newaccount_amount_from_account.select_option(value=str(cont_date["valid_account"]))
