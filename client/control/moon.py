from astral import moon
import datetime as datetimem
import math

MONTH=29.53

class Phase:
  def __init__(self,icon,day):
    self.icon=icon
    self.day=day

phases=[
  Phase('🌕',0),
  Phase('🌗',7),
  Phase('🌑',14),
  Phase('🌓',21),
]

def watch(now=False):
  now=now or datetimem.datetime.now()
  return moon.phase(now)

def get():
  day=watch()
  current=False
  for phase in reversed(phases):
    if day>=phase.day:
      current=phase
      break
  day=math.floor(day%7+1)
  return f'{day}/7 {current.icon}'

def track(datetime,now=False):
  now=now or datetimem.datetime.now()
  now-=datetimem.timedelta(days=watch(now))
  timedelta=now-datetime
  return f'{math.floor(timedelta.days/MONTH)+1}/3'
