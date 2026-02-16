import os
import time

from playwright.sync_api import Page

def salveaza_screenshot(page: Page, nume_fisier: str, folder):
    os.makedirs(folder, exist_ok=True)
    detalii_timp = time.strftime("%d%m%Y-%H%M%S")
    n_fisier = f"{nume_fisier}_{detalii_timp}.png"
    cale = f"{folder}/{n_fisier}"
    page.screenshot(path=cale)
    print(f"Screenshot salvat: {cale}")
    return cale