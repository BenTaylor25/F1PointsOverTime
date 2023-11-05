from datetime import datetime
from points_to_cumulative import points_to_cumulative

_points_sessions = {
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
    "brazil": 3,   # sprint only
    "vegas": 0,
    "abu_dhabi": 0,
}

_wiliams_weekends = {
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

dates = _points_sessions.values()

alphatauri_points = list(_alphatauri_weekends.values())
points_to_cumulative(alphatauri_points)

williams_points = list(_wiliams_weekends.values())
points_to_cumulative(williams_points)

alfa_romeo_points = list(_alfa_romeo_weekends.values())
points_to_cumulative(alfa_romeo_points)

haas_points = list(_haas_weekends.values())
points_to_cumulative(haas_points)
