from os import path, walk
import json
from datetime import datetime

DATA_PATH = "./points_data"
SEASON_FILE_EXTENSION = ".json"

def get_all_filenames():
    filenames = []

    for (_, _, walk_filenames) in walk(DATA_PATH):
        for filename in walk_filenames:
            filenames.append(filename)

    return filenames

def get_season_filename() -> str:
    filenames = get_all_filenames()

    for filename in filenames:
        print(f"- '{filename}'")

    while True:
        user_filename = input("Enter season filename: ")

        # Allow the user to omit file extension.
        if SEASON_FILE_EXTENSION not in user_filename:
            user_filename += SEASON_FILE_EXTENSION

        if user_filename not in filenames:
            print("Filename not recognised, try again.")
        else:
            return user_filename

def get_season_data():
    season_filename = get_season_filename()
    filepath = f"{DATA_PATH}/{season_filename}"

    if path.exists(filepath):
        with open(filepath) as f:
            deserialised_json = json.load(f)

        season = {
            "year": deserialised_json["year"],
            "dates": get_event_dates(deserialised_json),
            "team_names": get_team_names(deserialised_json),
            "team_colours": get_team_colours(deserialised_json),
            "team_points": get_team_points(deserialised_json)
        }

    return season

def get_event_dates(deserialised_json) -> list[datetime]:
    year = deserialised_json["year"]

    dates = []
    for event in deserialised_json["weekends"]:
        month = event["date"]["month"]
        day = event["date"]["day"]

        dates.append(datetime(year, month, day))

    return dates

def get_team_colours(deserialised_json) -> dict[str, str]:
    team_colours = dict()
    for team in deserialised_json["teams"]:
        team_colours[team["name"]] = team["hex_colour"]

    return team_colours

def get_team_points(deserialised_json) -> dict[str, list[int]]:
    teams = get_team_names(deserialised_json)
    weekends = deserialised_json["weekends"]

    team_points = dict()

    for team in teams:
        team_points[team] = []

    for weekend in weekends:
        for team in teams:
            team_points[team].append(weekend["points"][team])

    for team in team_points:
        cumulative(team_points[team])

    return team_points

def get_team_names(deserialised_json) -> list[str]:
    teams = []

    for team in deserialised_json["teams"]:
        teams.append(team["name"])

    return teams

def cumulative(numbers: list):
    for i in range (1, len(numbers)):
        numbers[i] += numbers[i - 1]
