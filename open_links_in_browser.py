import webbrowser
import pandas as pd
import sys

EMAILS_NOT_FOUND_FILE = "emailsNotFound.csv"
TITLE_NOT_FOUND = "NOT FOUND EMAILS CHANNELS"


if __name__ == "__main__":
    directory = sys.argv[1]
    links = pd.read_csv(directory + EMAILS_NOT_FOUND_FILE)

    for link in links[TITLE_NOT_FOUND]:
        webbrowser.open(link)
