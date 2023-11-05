
def points_to_cumulative(points: list):
    for i in range(1, len(points)):
        points[i] += points[i - 1]
