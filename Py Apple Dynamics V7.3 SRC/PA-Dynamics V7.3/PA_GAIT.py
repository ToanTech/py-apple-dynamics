import padog
import PA_STABLIZE
from math import pi,tan

x1=0;x2=0;x3=0;x4=0;y1=0;y2=0;y3=0;y4=0

def pit_cause_cg_adjust(sita,h,Kp):
  result=round((h*tan((sita)*Kp)),2)
  return result

def foward_cg_stab(r1,r4,r2,r3,gait_need,enable):
  if enable==True and (abs(r1)+abs(r4)+abs(r2)+abs(r3))!=0:  # When Key_stap set True in padog, self stab can be use here.
    PA_STABLIZE.get_imu_value()
    if PA_STABLIZE.gyro_cal_sta==1:   #等待gyro校准完成
      gyro_p=PA_STABLIZE.filter_data_p
      padog.X_goal=padog.in_y+gait_need+pit_cause_cg_adjust((gyro_p-PA_STABLIZE.p_origin)*pi/180,110,1.1)+PA_STABLIZE.gyro_x_fitted*5
      
def trot(t,x_target,z_target,r1,r4,r2,r3):
  global x1,x2,x3,x4,y1,y2,y3,y4
  Tf=0.5
  #陀螺仪引入
  foward_cg_stab(r1,r4,r2,r3,0,padog.key_stab)
  if t<Tf:
    phase_1_swing=padog.swing_curve_generate(t,Tf,x_target,z_target,0,0,0)
    phase_1_support=padog.support_curve_generate(0.5+t,Tf,x_target,0.5,0)
    #TROT
    x1=phase_1_swing[0]*r1;x2=phase_1_support[0]*r2;x3=phase_1_swing[0]*r3;x4=phase_1_support[0]*r4
    y1=phase_1_swing[1];y2=phase_1_support[1];y3=phase_1_swing[1];y4=phase_1_support[1]
    
  if t>=Tf:
    phase_2_swing=padog.swing_curve_generate(t-0.5,Tf,x_target,z_target,0,0,0)
    phase_2_support=padog.support_curve_generate(t,Tf,x_target,0.5,0)
    #TROT
    x1=phase_2_support[0]*r1;x2=phase_2_swing[0]*r2;x3=phase_2_support[0]*r3;x4=phase_2_swing[0]*r4
    y1=phase_2_support[1];y2=phase_2_swing[1];y3=phase_2_support[1];y4=phase_2_swing[1]
  return x1,x2,x3,x4,y1,y2,y3,y4



def walk(t,x_target,z_target,r1,r4,r2,r3):
  global x1,x2,x3,x4,y1,y2,y3,y4
  Tf=0.5
  #陀螺仪引入
  if t<Tf:
    foward_cg_stab(r1,r4,r2,r3,-30,True)
    if abs(padog.X_S-padog.X_goal)<1:
      padog.t=padog.t+padog.speed/5
      phase_w_swing=padog.swing_curve_generate(t,Tf,x_target,z_target,0,0,0)
      x1=phase_w_swing[0];x2=0;x3=0;x4=0
      y1=phase_w_swing[1];y2=0;y3=0;y4=0

  if t>=Tf and t<2*Tf:
    foward_cg_stab(r1,r4,r2,r3,-30,True)
    if abs(padog.X_S-padog.X_goal)<1:
      padog.t=padog.t+padog.speed/5
      phase_w_swing=padog.swing_curve_generate(t-0.5,Tf,x_target,z_target,0,0,0)
      x1=x_target;x2=phase_w_swing[0];x3=0;x4=0
      y1=0;y2=phase_w_swing[1];y3=0;y4=0
  
  if t>=2*Tf and t<3*Tf:
    foward_cg_stab(r1,r4,r2,r3,40,True)
    if abs(padog.X_S-padog.X_goal)<1:
      padog.t=padog.t+padog.speed/5
      phase_w_swing=padog.swing_curve_generate(t-1,Tf,x_target,z_target,0,0,0)
    
      x1=x_target;x2=x_target;x3=phase_w_swing[0];x4=0
      y1=0;y2=0;y3=phase_w_swing[1];y4=0

  if t>=3*Tf and t<4*Tf:
    foward_cg_stab(r1,r4,r2,r3,40,True)
    if abs(padog.X_S-padog.X_goal)<1:
      padog.t=padog.t+padog.speed/5
      phase_w_swing=padog.swing_curve_generate(t-1.5,Tf,x_target,z_target,0,0,0)
    
      x1=x_target;x2=x_target;x3=x_target;x4=phase_w_swing[0]
      y1=0;y2=0;y3=0;y4=phase_w_swing[1]

  if t>=4*Tf:
    foward_cg_stab(r1,r4,r2,r3,-30,True)
    padog.t=padog.t+padog.speed/5
    phase_w_support=padog.support_curve_generate(t-1.5,Tf,x_target,0.5,0)
    
    x1=phase_w_support[0];x2=phase_w_support[0];x3=phase_w_support[0];x4=phase_w_support[0]
    y1=phase_w_support[1];y2=phase_w_support[1];y3=phase_w_support[1];y4=phase_w_support[1]
    
  return x1,x2,x3,x4,y1,y2,y3,y4


