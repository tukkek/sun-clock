import tray.tray as traym
import os,PyQt6,datetime,season,webbrowser
import period as periodm
import moon as moonm

DEBUG=False
MINUTE=1*60
TICK=1 if DEBUG else MINUTE
CALENDAR='https://www.timeanddate.com/calendar/'

class Tray(traym.Tray):
  def update(self):
    now=datetime.datetime.now()
    period=periodm.get(now.hour)
    self.say(f'{period}.')
    path=f'icons/{period.lower().replace(' ','-')}.png'
    self.icon.setIcon(PyQt6.QtGui.QIcon(path))
    self.week.setText(moonm.get())
    self.season.setText(season.get())
    self.gregorian.setText(f'{now:%Y-%m-%d %H:%M}')

tray=Tray('Sun-Clock','icons/night.png',TICK)
tray.week=tray.act('Week')
tray.season=tray.act('Season')
gregorian=tray.act('Gregorian')
tray.gregorian=gregorian
gregorian.triggered.connect(lambda:webbrowser.open(CALENDAR))
tray.start()
