import pigpio

from time import sleep

LED_GPIO_PIN = 17 

pi = pigpio.pi()

level = 0

dir = 1

while True:
    pi.set_PWM_dutycycle(LED_GPIO_PIN, level)
    sleep(0.01)
    level += dir

    if level >= 255 or level <= 0:
        dir *= -1
