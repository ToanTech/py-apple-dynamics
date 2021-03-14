import padog
import socket
import PA_VMC
#-----------------------HTTP Server-----------------------#
user_leg_num="1"
url_cal="cal.html"
url_c="control.html"
thr=0;L=0;R=0;Pitch=padog.in_pit;Roll=padog.in_rol;Yst=padog.in_y;Hgt=100 #中间变量定义
url_n=url_c
g_s_num=100
addr = (padog.selfadd,80) #定义socket绑定的地址，ip地址为本地，端口为80
s = socket.socket()     #创建一个socket对象
s.bind(addr)            #绑定地址
s.listen(2)             #设置允许连接的客户端数量
print('listening on:', addr)
padog.gesture(Pitch,Roll,Yst)

while True:
    cl, addr = s.accept() #接受客户端的连接请求，cl为此链接创建的一个新的scoket对象，addr客户端地址
    #print('client connected from:', addr)
    req=str(cl.recv(1024))
    cl.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: FireBeetle\nContent-Type: text/html\n\n')
    req=req.split('\\r\\n')
    #http header 解析
    req_data=req[0].lstrip().rstrip().replace(' ','').lower()
    
    if req_data.find('favicon.ico')>-1:
        cl.close()
        continue
    else:
        req_data=req_data.replace('get/?','').replace('http/1.1','').replace("b'","")
        #print('req_data',req_data)
        if req_data.find('speed')>-1:
          print(req_data.replace('&',';'))
          exec(req_data.replace('&',';'))
          padog.l1=l1
          padog.l2=l2
          padog.l=l
          padog.b=b
          padog.w=w
          padog.speed=speed
          padog.h=h
          padog.kp_h=kp_h
          padog.kp_g=kp_g
          padog.ma_case=ma_case
          padog.vmc_mode=vmc_mode
        #ButtonKey
        index = req_data.find('key=')
        value = req_data[index+4:index+6].lstrip().rstrip()
        print('key:',value)
        #Pitch
        if req_data.find('pit=')>-1:
           index_p = req_data.find('pit=')
           value_p = req_data[index_p+4:index_p+7].lstrip().rstrip()
           if value_p!='/':
               #print('pit:',str(value_p))
               Pitch=int(value_p)
        #Roll
        if req_data.find('rol=')>-1:
           index_r = req_data.find('rol=')
           value_r = req_data[index_r+4:index_r+7].lstrip().rstrip()
           if value_r!='/':
               #print('rol:',str(value_r))
               Roll=int(value_r)
        #Height
        if req_data.find('hgt=')>-1:
           index_h = req_data.find('hgt=')
           value_h = req_data[index_h+4:index_h+7].lstrip().rstrip()
           if value_h!='/':
               print('hgt:',str(value_h))
               Hgt=int(value_h)
        #Y_controller
        if req_data.find('yst=')>-1:
           index_y = req_data.find('yst=')
           value_y = req_data[index_y+4:index_y+7].lstrip().rstrip()
           if value_y!='/':
               print('yst:',str(value_y))
               Yst=int(value_y)
        #运动控制用
        if value == 'go':
            print('thr:',thr)
            if thr<6:
                thr=thr+2
        elif value == 'ba':
            print('thr:',thr)
            if thr>-3:
                thr=thr-1
        elif value == 'le':
            thr=2
            L=-1;R=1
        elif value == 'ri':
            thr=2
            L=1;R=-1
        elif value == 'ss':
            url_n=url_cal
        elif value == 'gy':
            if padog.key_stab==True:
                padog.stable(False)
            else:
                padog.stable(True)
        elif value == 'qh':
            if padog.gait_mode==0:
                padog.gait(1)
                #顺带指定VMC中的P环值(walk)
                PA_VMC.KP_X=0.28
                PA_VMC.KP_Z=0.28
            else:
                padog.gait(0)
                #顺带指定VMC中的P环值(trot)
                PA_VMC.KP_X=0.47
                PA_VMC.KP_Z=0.47
                
        elif value == 'dm':
            thr=0;L=0;R=0
        elif value == 'ch':
            thr=0;L=1;R=1
        #标定判断用
        if value == 'l2':
            user_leg_num='2'
        elif value == 'l4':
            user_leg_num='4'
        elif value == 'l1':
            user_leg_num='1'
        elif value == 'l3':
            user_leg_num='3'
        elif value == 'sc':   #保存并退出
            s_f = open("config_s.py", "w+")
            #保存中位
            s_f.write("init_1h="+str(padog.init_1h)+"\n")
            s_f.write("init_1s="+str(padog.init_1s)+"\n")
            
            s_f.write("init_2h="+str(padog.init_2h)+"\n")
            s_f.write("init_2s="+str(padog.init_2s)+"\n")
                        
            s_f.write("init_3h="+str(padog.init_3h)+"\n")
            s_f.write("init_3s="+str(padog.init_3s)+"\n")
                        
            s_f.write("init_4h="+str(padog.init_4h)+"\n")
            s_f.write("init_4s="+str(padog.init_4s)+"\n")
            #保存机械、步态参数
            s_f.write("l1="+str(padog.l1)+"\n")
            s_f.write("l2="+str(padog.l2)+"\n")
            s_f.write("l="+str(padog.l)+"\n")
            s_f.write("b="+str(padog.b)+"\n")
            s_f.write("w="+str(padog.w)+"\n")
            s_f.write("speed="+str(padog.speed)+"\n")
            s_f.write("h="+str(padog.h)+"\n")
            s_f.write("Kp_H="+str(padog.Kp_H)+"\n")
            s_f.write("Kp_G="+str(padog.Kp_G)+"\n")
            s_f.write("ma_case="+str(padog.ma_case)+"\n")
            #保存初始位姿
            s_f.write("in_pit="+str(Pitch)+"\n")
            s_f.write("in_rol="+str(Roll)+"\n")
            s_f.write("in_y="+str(Yst)+"\n")
            #切换VMC/逆解模式
            s_f.write("vmc_mode="+str(padog.vmc_mode)+"\n")
            
            s_f.close()
            
            url_n=url_c
            padog.servo_init(0)
            padog.stand()
        elif value == 'hi':
            exec("padog.init_"+user_leg_num+"h="+"padog.init_"+user_leg_num+"h+1")
        elif value == 'hd':
            exec("padog.init_"+user_leg_num+"h="+"padog.init_"+user_leg_num+"h-1")
        elif value == 'si':
            exec("padog.init_"+user_leg_num+"s="+"padog.init_"+user_leg_num+"s+1")
        elif value == 'sd':
            exec("padog.init_"+user_leg_num+"s="+"padog.init_"+user_leg_num+"s-1")
        elif value == 't9':
            padog.servo_init(1)
    with open(url_n, 'r') as f:
        try:
            cl.sendall(f.read())
        except:
            pass
        if url_n=="cal.html":
          try:
            cl.send("""
            <center>
            <h1>控制器参数设定</h1>
            <br />
            <br />
            <form action="/" method="get" accept-charset="utf-8">
            """+
            """<br /><p>大腿(杆1)长　　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l1" """+"""value='"""+str(padog.l1)+"""'/></p>"""+\
            """<br /><p>小腿(杆2)长　　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l2" """+"""value='"""+str(padog.l2)+"""'/></p>"""+\
            """<br /><p>机器人长度　　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l" """+"""value='"""+str(padog.l)+"""'/></p>"""+\
            """<br /><p>机器人宽度　　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="b" """+"""value='"""+str(padog.b)+"""'/></p>"""+\
            """<br /><p>机器人腿间距 　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="w" """+"""value='"""+str(padog.w)+"""'/></p>"""+\
            """<br /><p>步频　　　 　　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="speed" """+"""value='"""+str(padog.speed)+"""'/></p>"""+\
            """<br /><p>抬腿高度　　　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="h" """+"""value='"""+str(padog.h)+"""'/></p>"""+\
            """<br /><p>高度调节系数　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="Kp_H" """+"""value='"""+str(padog.Kp_H)+"""'/></p>"""+\
            """<br /><p>姿态调节系数　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="Kp_G" """+"""value='"""+str(padog.Kp_G)+"""'/></p>"""+\
            """<br /><p>构型(0:串联 1:并连)   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="ma_case" """+"""value='"""+str(padog.ma_case)+"""'/></p>"""+\
            """<br /><p>VMC/逆解(0:逆解 1:VMC):&nbsp;<input type="text"  style="width:100px; height:30px;" name="vmc_mode" """+"""value='"""+str(padog.vmc_mode)+"""'/></p>"""+\
            """<br /><input type="Submit" style="width:100px; height:30px;" value="更改控制器参数"  />  """+\
            """</form>
            </center>
            </body>
            </html>
            """)
          except:
            pass
    cl.close()          #关闭socket
    #命令
    padog.move(thr,L,R)
    padog.height(Hgt)
    padog.gesture(Pitch,Roll,Yst)
    print('=========')
    print('Yst',Yst)
    print('Hgt',Hgt)
    print('Pitch',Pitch)
    print('Roll',Roll)





