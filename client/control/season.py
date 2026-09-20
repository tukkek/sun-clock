import datetime as datetimem
import json,pathlib

JSON=json.loads(pathlib.Path('flags.json').read_text())
NORTH=JSON['hemisphere'].lower()=='north'

class Season:
  def __init__(self,name,datetime):
    self.name=name
    self.datetime=datetime

def get():
  now=datetimem.datetime.now()
  year=now.year
  seasons=[
    Season('Winter',datetimem.datetime(year-1,12,21,12)),
    Season('Spring',datetimem.datetime(year,3,20,12)),
    Season('Summer',datetimem.datetime(year,6,20,12)),
    Season('Autumn',datetimem.datetime(year,9,22,12)),
    Season('Winter',datetimem.datetime(year,12,21,12)),
  ]
  current=False
  for season in reversed(seasons):
    if now>=season.datetime:
      current=season
      break
  if not NORTH:
    current=seasons[(seasons.index(current)+2)%4]
  return current
