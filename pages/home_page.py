from playwright.sync_api import Page, expect
from utils.utils_screenshot import salveaza_screenshot

class HomePage:
    
    def __init__(self,  page:Page):
        self.page = page
        self.newaccount_link = page.get_by_role("link", name="Open New Account")
        self.updatecontact_link = page.get_by_role("link", name="Update Contact Info")
        self.logout_link = page.get_by_role("link", name="Log Out")

    def verific_logged_in(self):
        try:
            #verific daca exista butonul de Log out
            expect(self.logout_link).to_be_visible(timeout=5000)
        except Exception:
            #eroare login, salvez screenshot-ul
            path = salveaza_screenshot(self.page, "login_esuat", "screenshots")
            raise AssertionError("Log in esuat. Screenshot salvat in: " + path)
        
    def click_new_account(self):
        self.newaccount_link.click()

    def click_update_contact(self):
        self.updatecontact_link.click()

    def click_logout(self):
        self.logout_link.click()
