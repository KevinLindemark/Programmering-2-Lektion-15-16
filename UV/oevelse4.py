from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pigpio

from time import sleep

LED_GPIO_PIN = 13

pi = pigpio.pi()

app = Flask(__name__)

socketio = SocketIO(app)

@socketio.on('skru')
def skru(data):
    lysstyrke = int(data['lysstyrke'])

    if lysstyrke < 0:
        lysstyrke = 0

    if lysstyrke > 255:
        lysstyrke = 255
    print(lysstyrke)
    pi.set_PWM_dutycycle(LED_GPIO_PIN, lysstyrke)

@app.route('/', methods=['GET'])
def index():
    return render_template('oevelse4.html')

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
