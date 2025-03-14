import base64
from io import BytesIO
from matplotlib.figure import Figure
from random import randint
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pigpio

BUTTON_GPIO_PIN = 4 

pi = pigpio.pi()
app = Flask(__name__)
socketio = SocketIO(app)

def tilstand():
    button_state = pi.read(BUTTON_GPIO_PIN)
    print(button_state)
    x = []
    y = []
    for i in range(10):
        x.append(randint(0, 10))
        y.append(randint(0, 10))
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x, y)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    print(data)
    socketio.emit('button_state', data)

@socketio.on('connect')
def connect():
    tilstand()

def cbf(gpio, level, tick):
    tilstand()

pi.callback(BUTTON_GPIO_PIN, pigpio.RISING_EDGE, cbf)
@app.route("/", methods=['GET'])

def hello():
    return render_template("bonus_matplot.html")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)


