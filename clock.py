#!/usr/bin/python3
import PyQt5.QtGui,PyQt5.QtWidgets,datetime,PyQt5.QtCore,dataclasses,sys,webbrowser

@dataclasses.dataclass
class Period:
  name:str
  hour:int
  
  def get(hour):
    while hour>23:
      hour-=24
    return next(p for p in periods if hour<p.hour+6)
  
periods=[Period('Night',0),Period('Morning',6),Period('Afternoon',12),Period('Evening',18)]  
a=PyQt5.QtWidgets.QApplication([])
i=PyQt5.QtWidgets.QSystemTrayIcon()
text=q=PyQt5.QtWidgets.QAction()
date=q=PyQt5.QtWidgets.QAction()

def describe(hours):
  return '1 hour' if hours==1 else f'{hours} hours'

def measure(hour):
  p=Period.get(hour)
  n=p.name.lower()
  if hour==p.hour:
    return p.name
  if hour-p.hour<3:
    return f'{describe(hour-p.hour)} past {n}'
  if hour-3==p.hour:
    return f'Late {n}'
  later=Period.get(p.hour+6)
  laterhour=later.hour
  if laterhour==0:
    laterhour=24
  return f'{describe(laterhour-hour)} to {later.name.lower()}'
  
def update():
  path='/'.join(sys.argv[0].split('/')[:-1])
  n=datetime.datetime.now()
  h=n.hour
  i.setIcon(PyQt5.QtGui.QIcon(f"{path}/icons/{h}.png"))
  tooltip=f'{measure(h)} ({h}:{n.minute:02})'
  i.setToolTip(tooltip)
  text.setText(tooltip)
  d=n.date()
  date.setText(f'{d.strftime("%A")}, {d.isoformat()}')
  
a.setQuitOnLastWindowClosed(False) 
m=PyQt5.QtWidgets.QMenu()
m.addAction(text)
m.addAction(date)
m.triggered.connect(lambda:webbrowser.open('https://www.timeanddate.com/calendar/'))
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
