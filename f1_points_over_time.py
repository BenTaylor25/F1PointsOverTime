from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from data import get_season_data
from utils import non_sprint_dates, highest_team_points

PLACEMENT_START = datetime(2023, 7, 3)
PLACEMENT_END = datetime(2024, 8, 2)

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
