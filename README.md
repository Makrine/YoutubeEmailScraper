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

Example:
```
python SteamAppsScraper.py "['Action', 'Adventure']" True 1 "D:/myDirectory/"


```
