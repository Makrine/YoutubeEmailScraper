import os
import googleapiclient.discovery
import googleapiclient.errors


def connect_api(key):
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl", "https://www.googleapis.com/auth/youtube.readonly"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        developerKey=key)
    return youtube
