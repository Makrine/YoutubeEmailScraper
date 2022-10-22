import urllib.request
import json
import steamfront
import random


def get_games(genres, number_of_games_to_get):
    client = steamfront.Client()
    with urllib.request.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0002") as url:
        data = json.loads(url.read().decode())
        with open("GameNames", "w", encoding="utf-8") as f:
            f.write("Name,Id,Genres\n")
            game_data = data["applist"]["apps"]
            count = 0
            while count < number_of_games_to_get:
                random_list = random.sample(game_data, number_of_games_to_get)
                for app in random_list:
                    try:
                        game = client.getApp(appid=str(app["appid"]))
                        if any((True for x in game.genres if x in genres)):
                            print(game.name)
                            link = f"https://store.steampowered.com/app/{str(app['appid'])}/{app['name']}"
                            f.write(app["name"] + ',' + str(app["appid"]) + ',' + str(game.genres) + ',' + link + '\n')
                            count += 1
                            if count == number_of_games_to_get:
                                break
                    except:
                        print("error: app wasn't found")
            f.close()

