#===头===
#1==-==2
#4==-==3
prep_time = 0.5#Duration before jumping [s]
launch_time = 0.7 #Duration before retracting the leg [s]
fall_time = 0.3#Duration after retracting leg to go back to normal behavior [s]
stance_height = 30# Desired leg extension before the jump [m]
jump_extension = -20 # Maximum leg extension in [m]
fall_extension = 30 #Desired leg extension during fall [m]


def cal_p(t,x_origin):
    if t < prep_time: 
        #print("prep")
        x1=x_origin;x2=x_origin;x3=x_origin;x4=x_origin
        y1=stance_height;y2=stance_height;y3=stance_height;y4=stance_height
        return x1,x2,x3,x4,y1,y2,y3,y4

    elif t >= prep_time and t < (prep_time + launch_time):  #起跳
        #print("launch_time")
        x1=x_origin;x2=x_origin;x3=x_origin;x4=x_origin
        y1=jump_extension;y2=jump_extension;y3=jump_extension;y4=jump_extension
        return x1,x2,x3,x4,y1,y2,y3,y4

    elif t >= (prep_time + launch_time) and t <= (prep_time + launch_time + fall_time):  #收腿待缓冲
        #print("fall_time")
        x1=x_origin;x2=x_origin;x3=x_origin;x4=x_origin
        y1=fall_extension;y2=fall_extension;y3=fall_extension;y4=fall_extension
        return x1,x2,x3,x4,y1,y2,y3,y4
    else:
        #print("else_time")
        return x_origin,x_origin,x_origin,x_origin,fall_extension,fall_extension,fall_extension,fall_extension
        

