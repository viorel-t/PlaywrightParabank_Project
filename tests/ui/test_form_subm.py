from playwright.sync_api import expect
from utils.utils_screenshot import salveaza_screenshot

def test_form_submission(auth_page):
    # Navighez către pagina cu formularul
    auth_page.goto("billpay.htm")
    try:
        # Verific daca pagina s-a incarcat corect
        expect(auth_page.get_by_role("link", name="Log Out")).to_be_visible(timeout=5000)
    except Exception:
        #eroare, acces pagina fara logare
        raise AssertionError("Form submission: nu s-a efectuat logarea.")

    # Completez câmpurile formularului
    auth_page.locator("input[name=\"payee.name\"]").fill("John Doe")
    auth_page.locator("input[name=\"payee.address.street\"]").fill("Str. Scurta 23")
    auth_page.locator("input[name=\"payee.address.city\"]").fill("Suceava")
    auth_page.locator("input[name=\"payee.address.state\"]").fill("SV")
    auth_page.locator("input[name=\"payee.address.zipCode\"]").fill("720229")
    auth_page.locator("input[name=\"payee.phoneNumber\"]").fill("0745123456")
    auth_page.locator("input[name=\"payee.accountNumber\"]").fill("123456789")
    auth_page.locator("input[name=\"verifyAccount\"]").fill("123456789")
    auth_page.locator("input[name=\"amount\"]").fill("10")
    auth_page.locator("select[name=\"fromAccountId\"]").select_option("13344")

    # Trimit formularul
    auth_page.get_by_role("button", name="Send Payment").click()

    try:
        # Verific daca mesajul de succes este afișat
        expect(auth_page.get_by_text("Bill Payment Complete")).to_be_visible(timeout=5000)
    except Exception:
        #eroare trimitere formular, salvez screenshot-ul
        path = salveaza_screenshot(auth_page, "bill_payment", "screenshots")
        raise AssertionError("Bill Payment esuat. Screenshot salvat in: " + path)