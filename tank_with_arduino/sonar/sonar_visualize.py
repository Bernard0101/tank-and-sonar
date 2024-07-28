import serial 
import matplotlib.pyplot as plt
import pygame
import numpy as np
import time


#port configuration
bluetooth_port = "/dev/ttyUSB0"
baud_rate = 9600;
timeout=1


#initilizing Serial communication
ser= serial.Serial(bluetooth_port, baud_rate, timeout=timeout)

pygame.mixer.init()
pygame.mixer.music.load('arduinos/tank_with_arduino/sonar/sonar_sound.mp3')
pygame.mixer.music.play()

positions=[]
distances=[]


#initial interactive plotting setup
try:
    plt.ion()
    fix, ax = plt.subplots(subplot_kw={'projection':'polar'})
    ax.set_facecolor('black')
    line_plot, = ax.plot([], [], 'r-', color='darkgreen')
    ax.set_title('interactive sonar', color='white')

    #loop for data reading
    while True:
        Serial_line = ser.readline().decode('utf-8', errors='ignore').strip()
        if Serial_line:
            try:
                pos, distance = map(int, Serial_line.split(','))
                print(f"position: {pos}")
                print(f"distance: {distance}")

                angle= np.radians(pos)

                positions = line_plot.get_xdata()
                distances = line_plot.get_ydata()
                positions = np.append(positions, angle)
                distances = np.append(distances, distance)
                
                 # Update plot data
                line_plot.set_xdata(positions)
                line_plot.set_ydata(distances)

                ax.relim()
                ax.autoscale_view()

                plt.draw()
                plt.pause(0.01)

                if len(distances) >= 175:
                    distances=distances[1:]
                    positions=positions[1:]


            except ValueError:
                print(f"Error could not read serial communication")

except KeyboardInterrupt:
    print("exiting")
finally:
    ser.close()
    plt.ioff()
    plt.show()