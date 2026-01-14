from playwright.sync_api import Page

class HomePage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.newaccount_link = page.get_by_role("link", name="Open New Account")
        self.updatecontact_link = page.get_by_role("link", name="Update Contact Info")
        self.logout_link = page.get_by_role("link", name="Log out")

        
    def click_new_account(self):
        self.newaccount_link.click()

    def click_update_contact(self):
        self.updatecontact_link.click()

    def click_logout(self):
        self.logout_link.click()
