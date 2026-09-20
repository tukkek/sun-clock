import tray.tray as traym
import os,PyQt6,datetime,webbrowser,calendar
import season as seasonm
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
    season=seasonm.get()
    month=moonm.track(season.datetime)
    self.season.setText(f'{month} {season.name.lower()}')
    gregorian=self.gregorian
    gregorian[2].setText(f'{now:%Y-%m-%d}')
    gregorian[1].setText(calendar.day_name[now.weekday()])
    gregorian[0].setText(f'{now:%H:%M}')

tray=Tray('Sun-Clock','icons/night.png',TICK)
tray.week=tray.act('Week')
tray.season=tray.act('Season')
tray.separate()
gregorian=[
  tray.act('Time'),
  tray.act('Day'),
  tray.act('Date'),
]
gregorian[2].triggered.connect(lambda:webbrowser.open(CALENDAR))
tray.gregorian=gregorian
tray.separate()
tray.start()
