# Retrieves emails from YouTube channels via searching queries,
# if those channels have included their email in description
# otherwise creates txt file for those channels we didn't get an email from

# Author: Makrine Tskipurishvili

from utils import *
from connection import *
from myCredential import *

if __name__ == "__main__":
    youtube = connect_api(KEY)
    retrieve_emails(youtube, "my youtube search query", max_results=10, min_views=10000)
