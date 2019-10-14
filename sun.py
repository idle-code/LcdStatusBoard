#!/usr/bin/env python3
import suncalc
from datetime import datetime

lat, lon = 53.13166, 23.1675  # Bialystok
current_time = datetime.now()
sun_times = suncalc.getTimes(current_time, lat, lon)

print("Sun rise: {}".format(sun_times['sunrise'].time().strftime("%H:%M")))
print("Sun set: {}".format(sun_times['sunset'].time().strftime("%H:%M")))

