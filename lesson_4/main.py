import requests
import random

page = random.randint(1, 7438)
pageSize = 1

def get_random_disney_character():
    response = requests.get("https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}")

    if response.status_code == 200:
        characters = response.json()["data"]

        character = random.choice(characters)

        print(f"Вам випав: {character['name']}")

        films = character.get("films", [])
        shorts = character.get("shortFilms", [])
        tv_shows = character.get("tvShows", [])
        video_games = character.get("videoGames", [])

        print("Фільми:")
        for film in films:
            print(f"- {film} -")

        print("\nКороткометражки:")
        for short in shorts:
            print(f"- {short} -")

        print("\nСеріали:")
        for tv_show in tv_shows:
            print(f"- {tv_show} -")

        print("\nІгри:")
        for game in video_games:
            print(f"- {game} -")
    else:
        print("Щось пішло не так...")
        print(f'{response.status_code=}')


if __name__ == "__main__":
    get_random_disney_character()