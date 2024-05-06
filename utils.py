from datetime import datetime

# For x-axis formatting.
def non_sprint_dates(dates: list[datetime]) -> list[datetime]:
    """
    Filter sprint race dates from list of dates.
    A sprint race occurs 1 day before the next date.
    """
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

# For y-axis formatting.
def highest_team_points(season) -> int:
    """
    Search a season team points
    """
    highest = 0

    for team_name in season["team_names"]:
        cum_team_points = season["team_points"][team_name]
        team_highest = cum_team_points[-1]

        highest = max(highest, team_highest)

    return highest
