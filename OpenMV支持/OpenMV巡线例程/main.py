import _thread
import padog
import time
from machine import Timer
from machine import UART
from padog import g,m
uart6=UART(2,115200)
t = Timer(1)
def OpenMV_Run(t):
  command=""
  DIS=0
  if uart6.any():
    read = uart6.read(1).decode('gbk')
    while read != '/':
      command = command + read
      read = uart6.read(1).decode('gbk')
    if(command != "1/" ) and command!="":
      try:
        exec(command)
        print("exec:",command)
      except:
        print("execerr:",command)
    command = ""


def app_1():
  exec(open('web_c.py').read())
  
def app_2():
  try:
    exec(open('my_code.py').read())
  except:
    print('积木编程代码执行出错，跳过...')

    
def loop(tt):
  padog.mainloop()
  
#_thread.start_new_thread(app_1, ())
#_thread.start_new_thread(app_2, ())
#_thread.start_new_thread(loop, ())
#t.init(period=10,mode=Timer.PERIODIC,callback=loop)


t.init(period=50,mode=Timer.PERIODIC,callback=OpenMV_Run)
padog.gesture(0,0,padog.in_y)
padog.speed=0.045
while True:
  padog.mainloop()
  '''
  try:
      OpenMV_Run(0)
  except:
    pass
  '''





