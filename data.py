from datetime import datetime
from points_to_cumulative import points_to_cumulative

_points_sessions = {
    "testing": datetime(2023, 2, 25),
    "bahrain": datetime(2023, 3, 5),
    "jeddah": datetime(2023, 3, 19),
    "australia": datetime(2023, 4, 2),
    "baku": datetime(2023, 4, 30),
    "miami": datetime(2023, 5, 7),
    "monaco": datetime(2023, 5, 28),
    "spain": datetime(2023, 6, 4),
    "canada": datetime(2023, 6, 18),
    "austria": datetime(2023, 7, 2),
    "silverstone": datetime(2023, 7, 9),
    "hungary": datetime(2023, 7, 23),
    "spa": datetime(2023, 7, 30),
    "zandvoort": datetime(2023, 8, 27),
    "monza": datetime(2023, 9, 3),
    "singapore": datetime(2023, 9, 17),
    "suzuka": datetime(2023, 9, 24),
    "qatar": datetime(2023, 10, 8),
    "usa": datetime(2023, 10, 22),
    "mexico": datetime(2023, 10, 29),
    "brazil": datetime(2023, 11, 5),
    "vegas": datetime(2023, 11, 18),
    "abu_dhabi": datetime(2023, 11, 26)
}

_alphatauri_weekends = {
    "testing": 0,
    "bahrain": 0,
    "jeddah": 0,
    "australia": 1,
    "baku": 1,
    "miami": 0,
    "monaco": 0,
    "spain": 0,
    "canada": 0,
    "austria": 0,
    "silverstone": 0,
    "hungary": 0,
    "spa": 1,
    "zandvoort": 0,
    "monza": 0,
    "singapore": 2,
    "suzuka": 0,
    "qatar": 0,
    "usa": 5,
    "mexico": 6,
    "brazil": 5,
    "vegas": 0,
    "abu_dhabi": 4,
}

_wiliams_weekends = {
    "testing": 0,
    "bahrain": 1,
    "jeddah": 0,
    "australia": 0,
    "baku": 0,
    "miami": 0,
    "monaco": 0,
    "spain": 0,
    "canada": 6,
    "austria": 0,
    "silverstone": 4,
    "hungary": 0,
    "spa": 0,
    "zandvoort": 4,
    "monza": 6,
    "singapore": 0,
    "suzuka": 0,
    "qatar": 2,
    "usa": 2,
    "mexico": 2,
    "brazil": 0,
    "vegas": 0,
    "abu_dhabi": 0,
}

_alfa_romeo_weekends = {
    "testing": 0,
    "bahrain": 4,
    "jeddah": 0,
    "australia": 2,
    "baku": 0,
    "miami": 0,
    "monaco": 0,
    "spain": 2,
    "canada": 1,
    "austria": 0,
    "silverstone": 0,
    "hungary": 0,
    "spa": 0,
    "zandvoort": 0,
    "monza": 1,
    "singapore": 0,
    "suzuka": 0,
    "qatar": 6,
    "usa": 0,
    "mexico": 0,
    "brazil": 0,
    "vegas": 0,
    "abu_dhabi": 0,
}

_haas_weekends = {
    "testing": 0,
    "bahrain": 0,
    "jeddah": 1,
    "australia": 6,
    "baku": 0,
    "miami": 1,
    "monaco": 0,
    "spain": 0,
    "canada": 0,
    "austria": 3,
    "silverstone": 0,
    "hungary": 0,
    "spa": 0,
    "zandvoort": 0,
    "monza": 0,
    "singapore": 1,
    "suzuka": 0,
    "qatar": 0,
    "usa": 0,
    "mexico": 0,
    "brazil": 0,
    "vegas": 0,
    "abu_dhabi": 0,
}

dates = list(_points_sessions.values())

alphatauri_points = list(_alphatauri_weekends.values())
points_to_cumulative(alphatauri_points)

williams_points = list(_wiliams_weekends.values())
points_to_cumulative(williams_points)

alfa_romeo_points = list(_alfa_romeo_weekends.values())
points_to_cumulative(alfa_romeo_points)

haas_points = list(_haas_weekends.values())
points_to_cumulative(haas_points)


# old ^

# new v
import os, json

DATA_PATH = "./points_data"

def get_season_data(year):
    filepath = f"{DATA_PATH}/{year}.json"

    if os.path.exists(filepath):
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
    teams = get_team_names(deserialised_json)

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

if __name__ == "__main__":
    get_season_data(2023)