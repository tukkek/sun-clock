#!/usr/bin/python3
import PyQt5.QtGui,PyQt5.QtWidgets,datetime,PyQt5.QtCore,dataclasses,sys,webbrowser,math

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
a=PyQt5.QtWidgets.QApplication([])
i=PyQt5.QtWidgets.QSystemTrayIcon()
text=q=PyQt5.QtWidgets.QAction()
date=q=PyQt5.QtWidgets.QAction()

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

def update():
  path='/'.join(sys.argv[0].split('/')[:-1])
  n=datetime.datetime.now()
  h=n.hour
  i.setIcon(PyQt5.QtGui.QIcon(f"{path}/icons/{h}.png"))
  tooltip=f'{measure(n)} ({h}:{n.minute:02})'
  i.setToolTip(tooltip)
  text.setText(tooltip)
  d=n.date()
  date.setText(f'{d.strftime("%A")}, {d.isoformat()}')
  
a.setQuitOnLastWindowClosed(False) 
m=PyQt5.QtWidgets.QMenu()
m.addAction(text)
m.addAction(date)
date.triggered.connect(lambda:webbrowser.open('https://www.timeanddate.com/calendar/'))
q=PyQt5.QtWidgets.QAction("Quit") 
q.triggered.connect(a.quit) 
m.addAction(q) 
i.setContextMenu(m) 
update()
i.setVisible(True)
t=PyQt5.QtCore.QTimer()
t.timeout.connect(update)
t.setInterval(60*1000)
t.start()
a.exec() 
