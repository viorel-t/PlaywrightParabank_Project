from playwright.sync_api import Page, expect

class UpdateProfilePage:   
    def __init__(self,  page:Page):
        self.page = page
        self.customer_fname = page.locator('input[name="customer.firstName"]')
        self.customer_lname = page.locator('input[name="customer.lastName"]')
        self.customer_streetaddress = page.locator('input[name="customer.address.street"]')
        self.customer_cityaddress = page.locator('input[name="customer.address.city"]')
        self.customer_stateaddress = page.locator('input[name="customer.address.state"]')
        self.customer_zipcode = page.locator('input[name="customer.address.zipCode"]')
        self.customer_phone = page.locator('input[name="customer.phoneNumber"]')
        self.updateprofile_button = page.get_by_role("button", name="Update Profile")

    def click_update_profile(self):
        self.updateprofile_button.click()

    def formular_fill(self, date_profil):
        self.customer_fname.fill(date_profil["f_name"])
        self.customer_lname.fill(date_profil["l_name"])
        self.customer_streetaddress.fill(date_profil["street"])
        self.customer_cityaddress.fill(date_profil["city"])        
        self.customer_stateaddress.fill(date_profil["state"])
        self.customer_zipcode.fill(date_profil["zip"])
        self.customer_phone.fill(date_profil["phone"])
