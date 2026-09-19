import tray.tray as traym
import os,PyQt6,datetime
import period as periodm

DEBUG=False
MINUTE=1*60
TICK=1 if DEBUG else MINUTE

class Tray(traym.Tray):
  def update(self):
    hour=datetime.datetime.now().hour
    period=periodm.get(hour)
    path=f'icons/{period.lower().replace(' ','-')}.png'
    self.icon.setIcon(PyQt6.QtGui.QIcon(path))
    self.say(period)

Tray('Sun-Clock','icons/night.png',TICK).start()
