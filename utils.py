import re
import os


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


def get_emails_from_channel(items, min_views, youtube):
    not_found_emails_list = []
    if os.path.exists("emailsNotFound.txt"):
        with open("emailsNotFound.txt", "r") as file:
            for line in file:
                not_found_emails_list.append(line.strip())

    for item in items:
        video_id = item["id"]["videoId"]

        if not video_info(video_id, min_views, youtube):  # if this video doesnt have enough views, pass
            pass

        emails_not_found = []  # channels for which we couldnt find email
        channel_id = item["snippet"]["channelId"]
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )

        response = request.execute()
        desc = response["items"][0]["snippet"]["description"]
        email = find_email(desc)

        if len(email) > 0:  # email found
            if not email[0][-1].isalpha():
                email = email[0][:-1]
        else:
            link = "https://www.youtube.com/channel/" + channel_id
            if link not in not_found_emails_list:
                emails_not_found.append(link)

        with open("emailsNotFound.txt", "a") as file:
            for i in emails_not_found:
                file.write('%s\n' % i)
            file.close()

        print(email)


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


def retrieve_emails(youtube, query, max_results, min_views):
    search_result = search(query, max_results, youtube)
    get_emails_from_channel(search_result, min_views, youtube)