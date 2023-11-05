import datetime
import random
import matplotlib.pyplot as plt

from data import dates
from data import alphatauri_points, williams_points, alfa_romeo_points, haas_points


# plot
plt.plot(dates, alphatauri_points)
plt.plot(dates, williams_points)
plt.plot(dates, alfa_romeo_points)
plt.plot(dates, haas_points)

# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()
