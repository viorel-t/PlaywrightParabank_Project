import os
import time

def save_api_response(url: str, raspuns: str, nume_fisier: str, extensie: str, folder):
    os.makedirs(folder, exist_ok=True)
    detalii_timp = time.strftime("%d%m%Y-%H%M%S")
    n_fisier = f"{nume_fisier}_{detalii_timp}.{extensie}"
    cale = f"{folder}/{n_fisier}"
    with open(cale, "w") as f:
        if extensie == "txt":
            f.write(f"URL: {url}\n")
            f.write(f"Status: {raspuns.status}\n")
            f.write(f"\nRaspuns: {raspuns.text()}")
        if extensie == "html":
            f.write(f"CONTENT-TYPE: {raspuns.headers.get('content-type')}\n\n")
            f.write(raspuns.text())
        if extensie == "xml":
            f.write(raspuns.text())
    return cale