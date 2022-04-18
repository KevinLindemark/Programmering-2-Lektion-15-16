import pigpio
from pigpio_dht import DHT11

from time import sleep

DHT11_PIN = 16

sensor = DHT11(DHT11_PIN) #, timeout_secs=10)

while True:
    print(sensor.read())
    sleep(2)
