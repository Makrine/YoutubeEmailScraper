# Retrieves emails from YouTube channels via searching queries,
# if those channels have included their email in description
# otherwise creates txt file for those channels we didn't get an email from

# Author: Makrine Tskipurishvili

from utils import *
from connection import *
# from myCredential import *
import sys

if __name__ == "__main__":
    youtube = connect_api(KEY)
    query = sys.argv[1]
    max_res = int(sys.argv[2])
    min_v = int(sys.argv[3])
    out = sys.argv[4]
    retrieve_emails(youtube, query, max_results=max_res, min_views=min_v, output_directory=out)
