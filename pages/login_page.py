from playwright.sync_api import Page

class LoginPage:
    
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator("input[name=\"username\"]")
        self.password_input = page.locator("input[name=\"password\"]")
        self.login_button = page.get_by_role("button", name="Log in")
        
    def enter_username(self, username: str):
        self.username_input.fill(username)
        
    def enter_password(self, password: str):
        self.password_input.fill(password)
        
    def click_login(self):
        self.login_button.click()
        
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()