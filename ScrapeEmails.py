# Retrieves emails from YouTube channels via searching queries,
# if those channels have included their email in description
# otherwise creates txt file for those channels we didn't get an email from

# Author: Makrine Tskipurishvili

from utils import *
from connection import *


if __name__ == "__main__":
    youtube = connect_api("AIzaSyCYubKtIAMDxAmwTN5o76NeRinmbMzYdhw")
    retrieve_emails(youtube, "The First Tree", 25, 10000)
