# Youtube And Steam Scraper

Retrieves emails from YouTube channels via search queries if those channels have included their email in description otherwise creates txt file for those channels we didn't get an email from


KEY is your API key.

# How To Use

1) install requirements 
```
pip install -r requirements.txt
```

## To get emails:
```
python ScrapeEmails.py "Search Query" maxResults minViews outputDirectory
```

Example:
```
python ScrapeEmails.py "The First Tree" 10 10000 "D:/myDirectory/"
```

(also incllude '/' at the end of the path)

## To open channels that we didn't get an email from:

ScrapeEmails creates a file called "emailsNotFound.csv" in the provided directory. It contains the links to channels that we didn't get an email from.

This will open all the links in the browser
```
python open_links_in_browser.py directory minIndex maxIndex"  
```

Example:
```
python open_links_in_browser.py "D:/myDirectory/" 0 5

```
This will open links from the file with indexes 0 to 5 (5 not inluded)

## to get game list with genres from steam:

```
python SteamAppsScraper.py listOfGenres matchALLOrANYgivenGenres numOfGamesToGet outputDirectory
```

if matchALLOrANYgivenGenres is set to True, the games that have both 'Action', 'Adventure' (any other genres too) will be retrived, if it is False then the games with either Action or Adventure or both will be retrieved (and + any other genre)
The accepted values for it are T or F

Example:
```
python SteamAppsScraper.py "['Action', 'Adventure']" T 1 "D:/myDirectory/"


```

# API KEY for Youtube API

1) go to [Google Console](https://console.cloud.google.com)
2) Create a project
3) Go to Library

![image](https://user-images.githubusercontent.com/66353680/197348674-fbf540f4-01e9-4e3f-bf61-e8d28835af26.png)

Search for "YouTube API" and add these two:

![image](https://user-images.githubusercontent.com/66353680/197348719-33d92974-a516-4c31-a5d2-6dc1e359caec.png)


5) Go to Credentials


![image](https://user-images.githubusercontent.com/66353680/197348196-fd450dfb-0a2f-46cc-952f-dca6eb9706c8.png)

4) Add API key


![image](https://user-images.githubusercontent.com/66353680/197348279-d80c7cba-ab44-46de-a1b1-3f3c49ddeda7.png)

5) Copy the key and replace KEY with it in ScrapeEmails.py as a string Ex: "someRandomLettersWhichAreTheKey"
(I have created myCredential.py for myself and put KEY = "myKEY")

