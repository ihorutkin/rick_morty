import requests
from django.db import IntegrityError

from characters.models import Character
from rick_and_morty.settings import RICK_AND_MORTY_API_CHARACTERS_URL


def scrape_characters() -> list[Character]:
    url_to_scrape = RICK_AND_MORTY_API_CHARACTERS_URL

    characters = []
    while url_to_scrape is not None:
        characters_response = requests.get(url_to_scrape).json()
        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict.get("id"),
                    name=character_dict.get("name"),
                    status=character_dict.get("status"),
                    species=character_dict.get("species"),
                    gender=character_dict.get("gender"),
                    image=character_dict.get("image"),
                )
            )
        url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(f"Character with api_id: {character.api_id} is already exist in DB")


def sync_characters_with_api():
    characters = scrape_characters()
    save_characters(characters)
