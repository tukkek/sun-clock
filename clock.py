#!/usr/bin/python3
import datetime,dataclasses,webbrowser,math,simple_tray.tray,PyQt5.QtWidgets,PyQt5.QtGui

MINUTE=60
HOUR=MINUTE*60

@dataclasses.dataclass
class Period:
  name:str
  hour:int
  
  def get(hour):
    while hour>23:
      hour-=24
    while hour<0:
      hour+=24
    return next(p for p in periods if hour<p.hour+6)
  
periods=[Period('Night',0),Period('Morning',6),Period('Afternoon',12),Period('Evening',18)]  

def describe(hours):
  return '1 hour' if hours==1 else f'{hours} hours'

def wind(hour,target,delta,now):
  d=datetime.datetime(now.year,now.month,now.day,hour=hour)
  while d.hour!=target.hour:
    d+=datetime.timedelta(hours=delta)
  return d

def drop(amount):
  if amount>10:
    amount=math.floor(amount/10)*10
  return math.floor(amount)

def measure(now):
  h=now.hour
  earlier=Period.get(h)
  earlierdelta=now-wind(h,earlier,-1,now)
  later=Period.get(h+6)
  laterdelta=wind(h,later,+1,now)-now
  reference=earlierdelta if earlierdelta<laterdelta else laterdelta
  hours=math.floor(reference.seconds/HOUR)
  length=f'{hours} hours' if hours>0 else f'{drop(reference.seconds/MINUTE)} minutes'
  if length.startswith('1 '):
    length=length[:-1]
  if reference==earlierdelta:
    return f'{length} into {earlier.name.lower()}' 
  return f'{length} until {later.name.lower()}'

class Tray(simple_tray.tray.Tray):
  def update(self):
    #path='/'.join(sys.argv[0].split('/')[:-1])
    n=datetime.datetime.now()
    h=n.hour
    self.icon.setIcon(PyQt5.QtGui.QIcon(f"icons/{h}.png"))
    tooltip=f'{measure(n)} ({h}:{n.minute:02})'
    self.say(tooltip)
    self.text.setText(tooltip)
    d=n.date()
    self.date.setText(f'{d.strftime("%A")}, {d.isoformat()}')
  
t=Tray('Sun-clock','',60)
t.text=q=PyQt5.QtWidgets.QAction()
t.menu.addAction(t.text)
t.date=q=PyQt5.QtWidgets.QAction()
t.date.triggered.connect(lambda:webbrowser.open('https://www.timeanddate.com/calendar/'))
t.menu.addAction(t.date)
t.start()
