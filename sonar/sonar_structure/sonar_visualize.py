import serial 
import matplotlib.pyplot
from drawnow import drawnow 
import time  

arduino_port = '/dev/ttyUSB0'
baud_rate = 9600
arduino_data = serial.Serial(arduino_port, baud_rate)
time.sleep(2)

angles = []
distances = []

def plot_sonar():
    # Plotar os dados como um gráfico de radar
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2)  # Alinhar o gráfico para cima
    ax.set_theta_direction(-1)  # Sentido anti-horário

    angles_rad = np.deg2rad(angles)  # Convertendo para radianos

    ax.plot(angles_rad, distances, color='b', linewidth=2)
    ax.fill(angles_rad, distances, color='b', alpha=0.3)

    # Configurações do gráfico
    ax.set_ylim(0, max(distances))
    ax.set_title('Sonar 180°', va='bottom')
    plt.draw()
    plt.pause(0.001)


def main():
    angles = []
    distances = []

    plt.ion()  # Ativar modo interativo
    fig = plt.figure()

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    angle, distance = map(int, line.split(','))
                    angles.append(angle)
                    distances.append(distance)

                    if angle == 180:  # Atualizar o gráfico a cada varredura completa
                        plot_sonar(angles, distances)
                        angles = []
                        distances = []
                except ValueError:
                    continue  # Ignorar linhas que não possam ser convertidas
    except KeyboardInterrupt:
        ser.close()
        print("Conexão serial encerrada.")
        plt.close()

