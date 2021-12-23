THRESHOLD = (0, 61, 19, 127, -128, 127)# Grayscale threshold for dark things...
import sensor, image, time
from machine import UART
uart=UART(1,115200)
from pid import PID
rho_pid = PID(p=0.4, i=0)
theta_pid = PID(p=0.001, i=0)
sensor.reset()
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQQVGA) # 80x60 (4,800 pixels) - O(N^2) max = 2,3040,000.
#sensor.set_windowing([0,20,80,40])
sensor.skip_frames(time = 2000)     # WARNING: If you use QQVGA it may take seconds
clock = time.clock()                # to process a frame sometimes.

while(True):
    clock.tick()
    time.sleep(100)
    img = sensor.snapshot().binary([THRESHOLD])
    line = img.get_regression([(100,100,0,0,0,0)], robust = True)
    if (line):
        rho_err = abs(line.rho())-img.width()/2
        if line.theta()>90:
            theta_err = line.theta()-180
        else:
            theta_err = line.theta()
        img.draw_line(line.line(), color = 127)
        #print(rho_err,line.magnitude(),rho_err)
        if line.magnitude()>8:
            #if -40<b_err<40 and -30<t_err<30:
            rho_output = rho_pid.get_pid(rho_err,1)
            theta_output = theta_pid.get_pid(theta_err,1)
            output = rho_output+theta_output
            #print(output)
            l_output=round((0.5-output/26),2)
            r_output=round((0.5+output/26),2)
            print("/m(2,"+str(l_output)+","+str(r_output)+")/")
            uart.write("/m(2,"+str(l_output)+","+str(r_output)+")/")
            pass
        else:
            print("/m(2,"+str(0)+","+str(0)+")/")
            #uart.write("/m(2,"+str(0)+","+str(0)+")/")
            pass
    else:
        #car.run(50,-50)
        pass
    #print(clock.fps())
