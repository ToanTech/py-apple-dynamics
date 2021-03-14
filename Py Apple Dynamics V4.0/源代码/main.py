import _thread
import padog
import time

def app_1():
  exec(open('web_c.py').read())


def loop():
  while True:
    padog.mainloop()

_thread.start_new_thread(app_1, ())

loop()

