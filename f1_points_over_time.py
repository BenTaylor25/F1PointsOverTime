from datetime import datetime
import matplotlib.pyplot as plt

from data import dates
from data import alphatauri_points, williams_points, alfa_romeo_points, haas_points


# plot
plt.plot(dates, alphatauri_points, '#010f1a', label="Scuderia AlphaTauri", linewidth=3)
plt.plot(dates, williams_points, '#00a1dd', label="Williams", linewidth=3)
plt.plot(dates, alfa_romeo_points, '#720a1e', label="Alfa Romeo", linewidth=3)
plt.plot(dates, haas_points, '#db2416', label="Haas", linewidth=3)

plt.axvline(x=datetime(2023, 7, 3), color='#000000', linestyle='--')

# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.legend()
plt.show()
