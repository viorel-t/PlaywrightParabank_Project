# Daca exista folderul history este copiat in allure-report
if (Test-Path "allure-report/history") {
    New-Item -ItemType Directory -Force "allure-results/history" | Out-Null
    Copy-Item -Recurse -Force "allure-report/history/*" "allure-results/history"
}

# Ruleaza testele
pytest --alluredir=allure-results

# Populare sectiunea Environment in Allure
@"
Browser=Chromium
Environment=Local
Base_URL=http://localhost:8080/parabank/
Base_URL_API=http://localhost:8080/parabank/services/bank/
OS=Windows 10
Python=3.13.2
Pytest=9.0.2
Playwright=1.57.0
allure-pytest=2.36.0
"@ | Set-Content -Path "allure-results/environment.properties"

@"
{
  "name": "Local Pytest Execution",
  "type": "local",
  "buildName": "Parabank UI + API Tests",
  "buildUrl": "",
  "reportName": "Allure Report - Parabank"
}
"@ | Set-Content -Path "allure-results/executor.json"


# Genereaza raportul Allure
allure generate allure-results -o allure-report --clean

# Deschide raportul in browser
allure open allure-report