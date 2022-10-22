import re
import os
import pandas as pd

EMAILS_NOT_FOUND_FILE = "emailsNotFound.csv"
EMAILS_FOUND_FILE = "emailsFound.csv"
EMAILS_LIST_FILE = "emailsList.csv"

TITLE_NOT_FOUND = "NOT FOUND EMAILS CHANNELS"
TITLE_FOUND = "FOUND EMAILS CHANNELS"
TITLE_EMAILS = "EMAILS"


def init_csvs(output_directory):
    if not os.path.exists(output_directory + EMAILS_NOT_FOUND_FILE):
        with open(output_directory + EMAILS_NOT_FOUND_FILE, "w") as f:
            f.write(TITLE_NOT_FOUND + "\n")
            f.close()
    if not os.path.exists(output_directory + EMAILS_FOUND_FILE):
        with open(output_directory + EMAILS_FOUND_FILE, "w") as f:
            f.write(TITLE_FOUND + "\n")
            f.close()
    if not os.path.exists(output_directory + EMAILS_LIST_FILE):
        with open(output_directory + EMAILS_LIST_FILE, "w") as f:
            f.write(TITLE_EMAILS + "\n")
            f.close()


def find_email(text):
    return re.findall('\S+@\S+', text)


def search(query, max_results, youtube):
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=query
    )

    response = request.execute()

    items = response["items"]

    return items


def read_list_if_file_exists(file, title, output_directory):
    my_list = []

    if os.path.exists(output_directory + file):
        my_file = pd.read_csv(output_directory + file)
        my_list = my_file[title]
    return my_list.values.tolist()


def write_list_to_file(my_list, file, title, output_directory):
    with open(output_directory + file, "w") as f:
        f.write(title + "\n")
        for i in my_list:
            f.write('%s\n' % i)
        f.close()


def append_channel_to_list_if_doesnt_exist(my_list, channel_id):
    link = "https://www.youtube.com/channel/" + channel_id + "/about"
    appended = False
    if link not in my_list:
        appended = True
        my_list.append(link)
    return my_list, appended


def write_emails_to_file(emails, file, output_directory):
    with open(output_directory + file, "a") as f:
        for i in emails:
            f.write('%s\n' % i)
        f.close()


def get_emails_from_channel(items, min_views, youtube, output_directory):
    not_found_emails_channels_list = read_list_if_file_exists(EMAILS_NOT_FOUND_FILE, TITLE_NOT_FOUND, output_directory)
    found_emails_channels_list = read_list_if_file_exists(EMAILS_FOUND_FILE, TITLE_FOUND, output_directory)
    emails = []

    for item in items:
        video_id = item["id"]["videoId"]

        if not video_info(video_id, min_views, youtube):  # if this video doesn't have enough views, pass
            pass

        channel_id = item["snippet"]["channelId"]
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )

        response = request.execute()
        desc = response["items"][0]["snippet"]["description"]
        email = find_email(desc)

        if len(email) > 0:  # email found
            found_emails_channels_list, added = append_channel_to_list_if_doesnt_exist(found_emails_channels_list, channel_id)

            if added:
                email = email[0]
                if not email[-1].isalpha():
                    email = email[:-1]
                emails.append(email)

        else:
            not_found_emails_channels_list, asd = append_channel_to_list_if_doesnt_exist(not_found_emails_channels_list,
                                                                                    channel_id)

    write_list_to_file(not_found_emails_channels_list, EMAILS_NOT_FOUND_FILE, TITLE_NOT_FOUND, output_directory)
    write_list_to_file(found_emails_channels_list, EMAILS_FOUND_FILE, TITLE_FOUND, output_directory)
    return emails


def video_info(video_id, min_views, youtube):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()
    views = response["items"][0]["statistics"]["viewCount"]

    if int(views) >= min_views:
        return True
    else:
        return False


def retrieve_emails(youtube, query, max_results, min_views, output_directory):
    init_csvs(output_directory)
    search_result = search(query, max_results, youtube)
    retrieved_emails = get_emails_from_channel(search_result, min_views, youtube, output_directory)
    write_emails_to_file(retrieved_emails, EMAILS_LIST_FILE, output_directory)
