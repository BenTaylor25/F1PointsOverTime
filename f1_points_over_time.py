from datetime import datetime
import matplotlib.pyplot as plt

from data import get_season_data

if __name__ == "__main__":
    season = get_season_data(2023)
    dates = season["dates"]

    for team_name in season["team_names"]:
        team_colour = season["team_colours"][team_name]
        team_points = season["team_points"][team_name]

        plt.plot(dates, team_points, team_colour, label=team_name, linewidth=3, marker='o')

    plt.axvline(x=datetime(2023, 7, 3), color='#000000', linestyle='--')

    today = datetime.today()
    if today < dates[-1]:
        plt.axvline(x=today, color='#000000', linestyle='--')


    # beautify the x-labels
    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.show()
