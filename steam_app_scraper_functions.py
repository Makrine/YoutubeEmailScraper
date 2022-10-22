import urllib.request
import json
import steamfront
import random


def get_games(genres, all_of_given_genres, number_of_games_to_get, output_directory):
    client = steamfront.Client()
    with urllib.request.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0002") as url:
        data = json.loads(url.read().decode())
        with open(output_directory + "GameNames.csv", "w", encoding="utf-8") as f:
            f.write("Name,Id,Genres,Link\n")
            game_data = data["applist"]["apps"]
            count = 0
            while count < number_of_games_to_get:
                random_list = random.sample(game_data, number_of_games_to_get)
                for app in random_list:
                    try:
                        game = client.getApp(appid=str(app["appid"]))
                        if all_of_given_genres:
                            if all(x in game.genres for x in genres):
                                print(game.name)
                                link = f"https://store.steampowered.com/app/{str(app['appid'])}/{app['name']}"
                                f.write(
                                    app["name"] + ',' + str(app["appid"]) + ',' + str(game.genres) + ',' + link + '\n')
                                count += 1
                                if count == number_of_games_to_get:
                                    break
                        else:
                            if any((True for x in game.genres if x in genres)):
                                print(game.name)
                                link = f"https://store.steampowered.com/app/{str(app['appid'])}/{app['name']}"
                                f.write(app["name"] + ',' + str(app["appid"]) + ',' + str(game.genres) + ',' + link + '\n')
                                count += 1
                                if count == number_of_games_to_get:
                                    break
                    except:
                        print(f"error: app with id {app['appid']} wasn't found. Ignore this.")
            f.close()

