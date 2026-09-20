# Solar Clock
A system-clock fully aligned with the Sun and Moon. It shows:
* Day-periods: night; morning; day and evening
* 7 days per lunar phase
* 3 lunar months per season
* Gregorian time; day and date (clicking the date opens a calendar)

Notifications are issued each 2 hours as the day-period changes. For example as early morning turns to morning then late morning.

# Rationale
It is impossible to track the Sun and Moon as independent bedies in a single system so lunisolar calendars ultimately settle for one.

For example the word *month* is derived from the *Moon* and its cycle but the gregorian week does not really align with its phases.

Solar Clock actually keeps track of both cycles with no compromise:
* The Sun dictates the day-period and seasons
* Months and weeks track the Moon

I call this a bilunisolar or concurrent-lunisolar calendar.

# Particularities
Each season counts the first day of new moons as a new month. 

Counted months start at 0/3 and end in 3/3. Rarely a season will end with 4/3 and very rare seasons may end with 2/3 months.

The week-day is based on the Moon and it starts roughly an hour later each day.

# Installing
You will need Git and Python (`apt-get install git python3`).

~~~sh
git clone --recursive https://github.com/tukkek/sun-clock
cd sun-clock/
python3 -m venv .venv/
.venv/bin/pip install --requirement requirements.txt
~~~

Next configure your system to run `launch.sh` from its folder when starting.
