from astral import moon
import datetime,math

class Phase:
  def __init__(self,icon,day):
    self.icon=icon
    self.day=day


phases=[
  Phase('🌑',0),
  Phase('🌓',7),
  Phase('🌕',14),
  Phase('🌗',21),
]

def get():
  day=moon.phase(datetime.datetime.now())
  current=False
  for phase in reversed(phases):
    if day>=phase.day:
      current=phase
      break
  day=math.floor(day%7+1)
  return f'{day}/7 {current.icon}'
