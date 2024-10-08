from steam_app_scraper_functions import *
import sys
import ast

if __name__ == "__main__":
    # get_games(genres=["RPG", "Action", "Adventure"], number_of_games_to_get=5)
    genres_list = ast.literal_eval(sys.argv[1])
    if sys.argv[2] == 'T':
        all_genres = True
    elif sys.argv[2] == 'F':
        all_genres = False
    else:
        print("Enter either T or F")
        sys.exit()

    number = int(sys.argv[3])
    out = sys.argv[4]
    get_games(genres=genres_list, all_of_given_genres=all_genres, number_of_games_to_get=number, output_directory=out)
