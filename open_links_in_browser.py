import webbrowser
import pandas as pd

EMAILS_NOT_FOUND_FILE = "emailsNotFound.csv"
TITLE_NOT_FOUND = "NOT FOUND EMAILS CHANNELS"

links = pd.read_csv(EMAILS_NOT_FOUND_FILE)

for link in links[TITLE_NOT_FOUND]:
    webbrowser.open(link)