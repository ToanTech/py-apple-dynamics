import _thread
import padog
import time
from machine import Timer

t = Timer(1)


def app_1():
  exec(open('web_c.py').read())

def loop():
  while True:
    padog.mainloop()
    
def loop2(t):
  padog.mainloop()
  
_thread.start_new_thread(app_1, ())
#_thread.start_new_thread(loop, ())
#loop()
t.init(period=10,mode=Timer.PERIODIC,callback=loop2)








