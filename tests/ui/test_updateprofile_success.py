import pytest
import allure
from pages.updateprofile_page import UpdateProfilePage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Test Update Profile Submission")
@allure.description("Verify user can update profile successfully.")
@allure.severity("normal")
@allure.epic("Web UI")
@allure.feature("Form Submission")
@allure.story("Valid update profile form submission")
def test_form_submission(auth_page, update_profile_data):
    update_profile_page = UpdateProfilePage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "updateprofile.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Completez câmpurile formularului
    update_profile_page.formular_fill(update_profile_data)
    
    # Trimit formularul
    update_profile_page.click_update_profile()

    # Verific mesajul de confirmare
    expect(auth_page.get_by_text("Profile Updated")).to_be_visible()