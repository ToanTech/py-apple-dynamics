import PA_IMU
from machine import SoftI2C, Pin
import padog

#中间变量定义
q=[]
Sta_Pitch=0
Sta_Roll=0
kp_sta=0.05
p_origin=0
r_origin=0
time_p=0
filter_data_p=0
filter_data_r=0
gyro_cal_sta=0
gyro_x_fitted=0
gyro_y_fitted=0
acc_z_fitted=0
#设置陀螺仪 IIC 接口

print("IMU启动中...")
i2cc = SoftI2C(scl=Pin(22), sda=Pin(21))   #集成板
acc = PA_IMU.accel(i2cc)
acc.error_gy()


def get_imu_value():
  global q,filter_data_p,filter_data_r,time_p,p_origin,r_origin,gyro_cal_sta,gyro_x_fitted,gyro_y_fitted,acc_z_fitted
  ay=acc.get_values()

  if time_p<=199:
    padog.alarm(50,300,500)
    if padog.PIT_goal!=0 or padog.ROL_goal!=0:
      padog.PIT_goal=0
      padog.ROL_goal=0
    else:
      try:
        p_origin=round(q[1])
        r_origin=round(q[2])
        time_p=time_p+1
        gyro_cal_sta=0
      except:
        time_p=0
        gyro_cal_sta=0
  elif time_p==200:
    padog.alarm(0,0,0)
    time_p=time_p+1
  else:
    try:
      filter_data_p = q[1]
      filter_data_r = q[2]
      gyro_x_fitted= ay["GyX"]/65.5*0.0174533  #输出P角速度
      gyro_y_fitted= ay["GyY"]/65.5*0.0174533  #输出P角速度
      acc_z_fitted=ay["AcZ"]/8192              #输出Z加速度
      gyro_cal_sta=1
    except:
      gyro_cal_sta=1
      
  q=PA_IMU.IMUupdate(ay["GyX"]/65.5*0.0174533,ay["GyY"]/65.5*0.0174533,ay["GyZ"]/65.5*0.0174533,ay["AcX"]/8192,ay["AcY"]/8192,ay["AcZ"]/8192)
    
      
def stab():
  global Sta_Pitch,Sta_Roll
  global p_origin,r_origin
  
  get_imu_value()
  
  Sta_Pitch=Sta_Pitch-(filter_data_p-p_origin)*padog.pit_Kp_G-gyro_x_fitted*padog.pit_Kd_G

  if Sta_Pitch>=padog.pit_max_ang: 
    Sta_Pitch=padog.pit_max_ang
  elif Sta_Pitch<=-padog.pit_max_ang: 
    Sta_Pitch=-padog.pit_max_ang

  Sta_Roll=Sta_Roll-(filter_data_r-r_origin)*padog.rol_Kp_G-gyro_y_fitted*padog.rol_Kd_G

  if Sta_Roll>=padog.rol_max_ang: 
    Sta_Roll=padog.rol_max_ang
  elif Sta_Roll<=-padog.rol_max_ang:
    Sta_Roll=-padog.rol_max_ang     
  
  if gyro_cal_sta==1:
    padog.PIT_goal=Sta_Pitch
    padog.ROL_goal=Sta_Roll
    padog.acc_z=acc_z_fitted
  else:   #清空防止跳动抖动
    Sta_Pitch=0
    Sta_Roll=0
    






















