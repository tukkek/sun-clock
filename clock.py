#!./venv/bin/python3
import PyQt5.QtGui,PyQt5.QtWidgets,datetime,PyQt5.QtCore,dataclasses

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

def update(hourp=None):
  n=datetime.datetime.now()
  h=hourp if hourp!=None else n.hour
  m=n.minute
  i.setIcon(PyQt5.QtGui.QIcon(f"icons/{h}.png"))
  p=Period.get(h)
  later=Period.get(p.hour+6)
  laterhour=later.hour
  if laterhour==0:
    laterhour=24
  tooltip=f'{h-p.hour} hours past {p.name}'if h-p.hour<3 else f'{laterhour-h} hours to {later.name}'
  tooltip=f'{tooltip.lower()}, {h}:{m:02}'
  print(h,tooltip)
  i.setToolTip(tooltip)
  text.setText(tooltip)

a.setQuitOnLastWindowClosed(False) 
m=PyQt5.QtWidgets.QMenu() 
m.addAction(text) 
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

for hour in range(0,24):
  update(hour)

a.exec() 
