# PlaywrightParabank_Project
Testing Parabank application with Playwright and Pytest.

- Am identificat ca Parabank permite transferul intre acelasi cont sursa si destinatie
(test_fund_transfer_same_account.py: success !!!)

- Pentru valori ca 0 sau negative, aplicatia permite plata, ceea ce este un comportament incorect. Testele mele evidențiază acest defect prin rezultate FAIL.
(test_billpay_amount_zero.py, test_billpay_amount_negative.py)

- Aplicatis permite valori negative sau 0 la transferuri desi nu ar trebui sa proceseze cererea.
(test_post_fundTransfer_invalid_amount.py: permite !!!)

- ParaBank face ca la retrageri negative sa creasca soldul (depuneri mascate) !!!
(test_post_withdraw_funds_negAmo.py: permite !!!)

- Transfer fonduri, la lipsa amount → bug/ aplicatia crapa (internal error)
(test_post_fundTransfer_missing_param.py: crash !!!)

-Security issue: credentiale necriptate
(test_get_custDetails.py: credentiale in URL !!!)