#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0
from math import sin,cos,pi,atan,tan

# PID参数设置
KP_S=0.02    #扭矩-舵机角速度P环
KP_X=0.47     #X坐标控制器P环（初始，适用于trot）
KP_Z=0.47     #Z坐标控制器P环（初始，适用于trot）
KD_X=0.0     #X坐标控制器D环
KD_Z=0.0     #Z坐标控制器D环

Vx=0;Vz=0  #暂时不引入速度反馈，但保留接口

# 部分中间参数
leg1_X_N=0;leg2_X_N=0;leg3_X_N=0;leg4_X_N=0
leg1_Z_N=100;leg2_Z_N=100;leg3_Z_N=100;leg4_Z_N=100
leg1_ham_origin=130.5188;leg2_ham_origin=130.5188;leg3_ham_origin=130.5188;leg4_ham_origin=130.5188
leg1_shank_origin=-91.7463;leg2_shank_origin=-91.7463;leg3_shank_origin=-91.7463;leg4_shank_origin=-91.7463
leg1_X_last=leg1_X_N;leg2_X_last=leg2_X_N;leg3_X_last=leg3_X_N;leg4_X_last=leg4_X_N  #通过原默认坐标值设定初始值
leg1_Z_last=leg1_Z_N;leg2_Z_last=leg2_Z_N;leg3_Z_last=leg3_Z_N;leg4_Z_last=leg4_Z_N  #通过原默认坐标值设定初始值


def cal_vmc_single_leg(l1,l2,ham1_origin,shank1_origin,Xe,Ze,X,Z,Xl,Zl):
    # PD 控制器
    Vx=X-Xl
    Vz=Z-Zl
    Fx=KP_X*(Xe-X)+KD_X*(0-Vx)
    Fy=KP_Z*(Ze-Z)+KD_Z*(0-Vz)
    #保存上一个位置参数，用来在下一次循环求速度
    X_last=X
    Z_last=Z
    #角度转弧度
    ham1=ham1_origin*pi/180
    shank1=shank1_origin*pi/180
    # 求力矩
    tham1= - Fy*(l2*cos(ham1)*sin(shank1) + l2*cos(shank1)*sin(ham1)) - Fx*(l1*sin(ham1) + l2*cos(ham1)*sin(shank1) + l2*cos(shank1)*sin(ham1))
    tshank1= Fy*(l2*cos(ham1)*cos(shank1) - l2*sin(ham1)*sin(shank1)) + Fx*(l1*cos(ham1) + l2*cos(ham1)*cos(shank1) - l2*sin(ham1)*sin(shank1))
    s_o_tham1=tham1*KP_S
    s_o_tshank1=tshank1*KP_S
    
    # 更新新的关节角度，准备求正解
    ham1_origin=ham1_origin+s_o_tham1
    shank1_origin=shank1_origin+s_o_tshank1
    # 正解（虚拟反馈器或者编码器，输出目前足端坐标位置）
    x1_d=l1*cos(ham1_origin*pi/180)
    y1_d=l1*sin(ham1_origin*pi/180)

    x2_d=x1_d+cos(ham1_origin*pi/180)*cos(shank1_origin*pi/180)*l2-sin(ham1_origin*pi/180)*sin(shank1_origin*pi/180)*l2
    y2_d=y1_d+sin(ham1_origin*pi/180)*cos(shank1_origin*pi/180)*l2+cos(ham1_origin*pi/180)*sin(shank1_origin*pi/180)*l2

    #输出舵机控制角速度
    return s_o_tham1,s_o_tshank1,x2_d,y2_d,X_last,Z_last
    
def cal_v(case,l1,l2,x1,x2,x3,x4,y1,y2,y3,y4):
    global leg1_ham_origin,leg2_ham_origin,leg3_ham_origin,leg4_ham_origin
    global leg1_shank_origin,leg2_shank_origin,leg3_shank_origin,leg4_shank_origin
    global leg1_X_N,leg2_X_N,leg3_X_N,leg4_X_N
    global leg1_Z_N,leg2_Z_N,leg3_Z_N,leg4_Z_N
    global leg1_X_last,leg2_X_last,leg3_X_last,leg4_X_last
    global leg1_Z_last,leg2_Z_last,leg3_Z_last,leg4_Z_last
    
    #变换坐标符号
    #x1=-x1;x2=-x2;x3=-x3;x4=-x4
    y1=-y1;y2=-y2;y3=-y3;y4=-y4
    #传参进入VMC计算器计算
    A_1=cal_vmc_single_leg(l1,l2,leg1_ham_origin,leg1_shank_origin,x1,y1,leg1_X_N,leg1_Z_N,leg1_X_last,leg1_Z_last)
    A_2=cal_vmc_single_leg(l1,l2,leg2_ham_origin,leg2_shank_origin,x2,y2,leg2_X_N,leg2_Z_N,leg2_X_last,leg2_Z_last)
    A_3=cal_vmc_single_leg(l1,l2,leg3_ham_origin,leg3_shank_origin,x3,y3,leg3_X_N,leg3_Z_N,leg3_X_last,leg3_Z_last)
    A_4=cal_vmc_single_leg(l1,l2,leg4_ham_origin,leg4_shank_origin,x4,y4,leg4_X_N,leg4_Z_N,leg4_X_last,leg4_Z_last)
    
    #加入角速度，散点积分得到舵机角度
    #腿1
    leg1_ham_origin=leg1_ham_origin+A_1[0]
    leg1_shank_origin=leg1_shank_origin+A_1[1]
    #腿2
    leg2_ham_origin=leg2_ham_origin+A_2[0]
    leg2_shank_origin=leg2_shank_origin+A_2[1]
    #腿3
    leg3_ham_origin=leg3_ham_origin+A_3[0]
    leg3_shank_origin=leg3_shank_origin+A_3[1]
    #腿4
    leg4_ham_origin=leg4_ham_origin+A_4[0]
    leg4_shank_origin=leg4_shank_origin+A_4[1]
    #模拟传感器反馈现在的腿位置
    #腿1
    leg1_X_N=A_1[2]
    leg1_Z_N=A_1[3]
    #腿2
    leg2_X_N=A_2[2]
    leg2_Z_N=A_2[3]
    #腿3
    leg3_X_N=A_3[2]
    leg3_Z_N=A_3[3]
    #腿4
    leg4_X_N=A_4[2]
    leg4_Z_N=A_4[3]
    #记录前一时刻腿位置，用于计算速度
    #腿1
    leg1_X_last=A_1[4]
    leg1_Z_last=A_1[5]
    #腿2
    leg2_X_last=A_2[4]
    leg2_Z_last=A_2[5]
    #腿3
    leg3_X_last=A_3[4]
    leg3_Z_last=A_3[5]
    #腿4
    leg4_X_last=A_4[4]
    leg4_Z_last=A_4[5]
    '''
    print('leg1_X_N:',leg1_X_N)
    print('leg1_Z_N:',leg1_Z_N)
    print('leg1_ham_origin',leg1_ham_origin)
    print('leg1_shank_origin',leg1_shank_origin)
    print('height',height)
    '''
    #输出到舵机
    return 180-leg1_ham_origin,180-leg2_ham_origin,180-leg3_ham_origin,180-leg4_ham_origin,-leg1_shank_origin,-leg2_shank_origin,-leg3_shank_origin,-leg4_shank_origin







