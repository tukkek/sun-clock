# Sun Clock
Sun Clock is a simple 24-hour system-tray clock that has noon as the top-most position (representing the zenith of the Sun in the sky) and that runs counter-clock-wise, like the Sun rising from the east.

Hovering or right-clicking the icon will show the exact 24-hour time and describe the current time in relation to night (0:00-5:00), morning (6:00-11:00), day (12:00-17:00) and evening (18:00-23:00).

It's a simpler way to organize the passing of the day in accordance to natural time, compared to the arbitrary 24-hours of the clock. It's probably not for most people but perhaps a more Zen time-keeping.

# Installation
Execute the following commands:
```sh
git clone --recurse-submodules https://github.com/tukkek/sun-clock
cd sun-clock/
python3 -m venv .venv/
.venv/bin/pip install -r requirements.txt
```

You can optionally configure Sun Clock to start automatically (consult your operating-system documentation) and also remove your system clock if you don't want two clocks running at the same time. For this purpose: you can use a command like: `/path/to/sun-clock/.venv/bin/python /path/to/sun-clock/clock.py`.
