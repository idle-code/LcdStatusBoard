#!/usr/bin/env python3
import suncalc
from datetime import datetime

lat, lon = 53.13166, 23.1675  # Bialystok
current_time = datetime.now()
#sun_times = suncalc.getTimes(current_time, lat, lon)
moon_times = suncalc.getMoonTimes(current_time, lat, lon)
moon_phase = suncalc.getMoonIllumination(current_time)

print("Moon rise: {}".format(moon_times['rise'].time().strftime("%H:%M")))
print("Fraction: {:.0%}".format(moon_phase['fraction']))

