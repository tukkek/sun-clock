#!./venv/bin/python3
import PyQt5.QtGui,PyQt5.QtWidgets,datetime,PyQt5.QtCore
  
a=PyQt5.QtWidgets.QApplication([])
i=PyQt5.QtWidgets.QSystemTrayIcon()
text=q=PyQt5.QtWidgets.QAction()

def update():
  n=datetime.datetime.now()
  m=n.minute
  h=n.hour
  i.setIcon(PyQt5.QtGui.QIcon(f"icons/{h}.png"))
  tooltip=f'{h}:{m:02}'
  i.setToolTip(tooltip)
  text.setText(tooltip)
  print(tooltip)

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
t.setInterval(1*1000)
t.start()
a.exec() 
