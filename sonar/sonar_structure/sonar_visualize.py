import serial 
import matplotlib.pyplot as plt
import time


#port configuration
bluetooth_port = "/dev/ttyUSB0"
baud_rate = 9600;
timeout=1

#initilizing Serial communication
ser= serial.Serial(bluetooth_port, baud_rate, timeout=timeout)

positions=[]
distances=[]

#initial interactive plotting setup
try:
    plt.ion()
    fix, ax = plt.subplots()
    line_plot, = ax.plot([], [], 'r-')
    ax.set_xlabel('distance (cm)')
    ax.set_ylabel('position of servo (degrees)')
    ax.set_title('interactive sonar')
    ax.grid(True)

    #loop for data reading
    while True:
        Serial_line = ser.readline().decode('utf-8', errors='ignore').strip()
        if Serial_line:
            try:
                pos, distance = map(int, Serial_line.split(','))
                print(f"position: {pos}")
                print(f"distance: {distance}")
                distances.append(distance)
                positions.append(pos)

                #update plots data
                line_plot.set_xdata(distances)
                line_plot.set_ydata(positions)
                ax.relim()
                ax.autoscale_view()

                plt.draw()
                plt.pause(0.01)


            except ValueError:
                print(f"Error could not read serial communication")

except KeyboardInterrupt:
    print("exiting")
finally:
    ser.close()
    plt.ioff()
    plt.show()