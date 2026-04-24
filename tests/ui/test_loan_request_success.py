import pytest
import allure
from pages.requestloan_page import RequestLoanPage
from config import URL_BAZA
from playwright.sync_api import expect

@pytest.mark.form
@pytest.mark.ui
@allure.title("Successful loan request")
@allure.description("""Verify that a logged-in user can successfully request a loan using valid input data.""")
@allure.severity("critical")
@allure.epic("Web UI")
@allure.feature("Loans")
@allure.story("Request Loan")
def test_form_submission(auth_page, request_loan_load):
    request_loan_page = RequestLoanPage(auth_page)
    
    # Navighez către pagina cu formularul
    auth_page.goto(URL_BAZA + "requestloan.htm")
    
    # Verific ca userul este logat
    expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible()

    # Confirm ca sunt in RequestLoan Page
    expect(auth_page.get_by_role("heading", name="Apply for a Loan")).to_be_visible()

    # Completez formularul de imprumut
    request_loan_page.fill_loan_form(request_loan_load)

    # Trimit formularul - efectuez request-ul
    request_loan_page.click_requestloan()

    # Verific mesajul de confirmare a imprumutului (aprobare)
    expect(auth_page.get_by_role("heading", name="Loan Request Processed")).to_be_visible()
    expect(auth_page.locator("#loanStatus")).to_have_text("Approved")
    
    # Verific ca s-a creat un cont nou
    cont_nou = auth_page.locator("#newAccountId")
    assert cont_nou.is_visible()
    
    # id-ul contului nu e gol si e numeric
    account_id = cont_nou.text_content()
    assert account_id is not None
    assert account_id.isdigit()