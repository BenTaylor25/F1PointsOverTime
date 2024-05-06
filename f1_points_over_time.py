from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from data import get_season_data

PLACEMENT_START = datetime(2023, 7, 3)
PLACEMENT_END = datetime(2024, 8, 2)

def highest_team_points(season) -> int:
    highest = 0

    for team_name in season["team_names"]:
        team_points = season["team_points"][team_name]
        team_highest = max(team_points)

        highest = max(highest, team_highest)

    return highest

def non_sprint_dates(dates: list[datetime]) -> list[datetime]:
    sprint_dates = []

    for i, date in enumerate(dates):
        # Ignore last date.
        if date == dates[-1]:
            break

        next_date = dates[i + 1]

        days_between = (next_date - date).days

        if days_between == 1:
            sprint_dates.append(date)

    # Filter sprint_dates from dates.
    non_sprint_dates = [date for date in dates if date not in sprint_dates]

    return non_sprint_dates

if __name__ == "__main__":
    season = get_season_data()
    dates = season["dates"]

    for team_name in season["team_names"]:
        team_colour = season["team_colours"][team_name]
        team_points = season["team_points"][team_name]

        plt.plot(dates, team_points, team_colour, label=team_name, linewidth=3, marker='o')

    if season["year"] == 2023:
        plt.axvline(x=PLACEMENT_START, color='#000000', linestyle='--')
    elif season["year"] == 2024:
        if datetime.today() >= PLACEMENT_END:
            plt.axvline(x=PLACEMENT_END, color='#000000', linestyle='--')

    today = datetime.today()
    if today < dates[-1]:
        plt.axvline(x=today, color='#000000', linestyle='--')


    # Format the x-labels.
    plt.gcf().autofmt_xdate()
    plt.xticks(non_sprint_dates(dates))

    # Use whole numbers for y-axis.
    plt.yticks(np.arange(0, highest_team_points(season) + 1, 1.0))

    plt.legend()
    plt.show()
