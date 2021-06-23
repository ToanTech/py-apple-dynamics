#=====使用方法：
#ESP32 18,5,17,16 分别接航模遥控器PWM:CH1 CH2 CH3 CH7
#默认针对左手油门遥控器开发
#=====遥控器操控
#油门：调节踏步高度
#右手前后推摇杆：控制前进后退
#右手左右推摇杆：控制左右
#CH7：控制踏步开/关
from machine import time_pulse_us
from machine import Pin
from machine import Timer
import time
import padog
from math import floor
from math import ceil


#初始参数读取/设定
Pitch=0;Roll=0;Yst=padog.in_y;Hgt=110
padog.height(Hgt)
padog.gesture(Pitch,Roll,Yst)

#启动定时器
t = Timer(1)
t1 = Timer(2)

def loop(t1):
  padog.mainloop()

def fb_curve(x):        #前进后退遥控器曲线标定
  p1 =   5.334e-06
  p2 =    -0.02423
  p3 =       23.92
  return p1*x*x + p2*x + p3

def leg_lh_curve(x):    #踏步高低遥控器曲线标定
  p1 =     0.02006
  p2 =       6.184
  return p1*x + p2

def leg_t_curve(x):     #转向遥控器曲线标定
  p1 =    0.002006
  p2 =      -3.002
  return (p1*x + p2)*0.6

def remoter(t):         #遥控器信号解算程序
  micros1 = time_pulse_us(Pin(18,Pin.IN), 1)  #CH1 转左转右
  micros2 = time_pulse_us(Pin(5,Pin.IN), 1)   #CH2 前进后退
  micros3 = time_pulse_us(Pin(17,Pin.IN), 1)  #CH3 油门（抬腿高度）
  micros4 = time_pulse_us(Pin(16,Pin.IN), 1)  #CH7 模式切换
  if micros4<1500:
    padog.h=floor(leg_lh_curve(micros3))
    if micros1<=(1500-200):     #左转
      #padog.move(2,1-abs((micros1-1500)/250),1)
      padog.move(2.5,-1,1)
    elif micros1>=(1500+200):     #右转
      padog.move(2.5,1,-1)
      #padog.move(2,1,1-abs((micros1-1500)/250))
    else:
      padog.move(floor(fb_curve(micros2)),1,1)
  else:
    padog.move(0,0,0)
  


t.init(period=130,mode=Timer.PERIODIC,callback=remoter)   #遥控器定时器
t1.init(period=10,mode=Timer.PERIODIC,callback=loop)      #控制心跳定时器

