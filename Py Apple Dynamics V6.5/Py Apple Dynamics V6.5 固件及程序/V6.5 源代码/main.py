import _thread
import padog
import time
from machine import Timer

t = Timer(1)

def loop(t):
  padog.mainloop()

def app_1():
  exec(open('web_c.py').read())

_thread.start_new_thread(app_1, ())
t.init(period=10,mode=Timer.PERIODIC,callback=loop)


