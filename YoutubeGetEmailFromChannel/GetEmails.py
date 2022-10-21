import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import re
import json
import requests
from bs4 import BeautifulSoup


def get_path():
    global v
    csv_file_path = askopenfilename()
    v.set(csv_file_path)


def get_csv_data():
    global v
    file = pd.read_csv(v.get())
    return file["links"].values


def find_email(text):
    return re.findall('\S+@\S+', text)


def retrieve_email(data):
    altered_data = []
    for d in data:
        d = d + "/about"
        altered_data.append(d)

    emails = []

    for d in altered_data:
        soup = BeautifulSoup(requests.get(d).content, "html.parser")

        # We locate the JSON data using a regular-expression pattern
        data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)
        json_data = json.loads(data)
        stats = json_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][5]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"]

        desc = stats["description"]["simpleText"]
        email = find_email(desc)

        # if not email[0][-1].isalpha():
        #     email = email[0][:-1]
        emails.append(email)

    return emails


def write_to_file(emails):
    with open("emails.csv", 'w+') as file:
        file.writelines("emails\n")
        for email in emails:
            file.writelines(email)
            file.write('\n')
        file.close()


def do_the_thing():
    data = get_csv_data()
    emails = retrieve_email(data)
    write_to_file(emails)
    tk.Label(root, text='Done, check emails.csv file').grid(row=2, column=1)


root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set', command=get_path).grid(row=1, column=0)
tk.Button(root, text='Get Emails', command=do_the_thing).grid(row=1, column=1)

root.mainloop()
