import pigpio
from time import sleep
pi = pigpio.pi()

KNAP_GPIO = 4
LED_GPIO = 17

pi.set_PWM_range(LED_GPIO, 100)
duty_val = 0

direction = 1

while True:
    first = pi.read(KNAP_GPIO)
    sleep(0.001)
    second = pi.read(KNAP_GPIO)
    if first and not second:
        print(pi.get_PWM_dutycycle(LED_GPIO))
        duty_val += direction *10
        sleep(0.1)
        if duty_val > 0 and duty_val <= 100:
            pi.set_PWM_dutycycle(LED_GPIO, duty_val)
        else:
            print("Max/Min duty")
            direction *= -1
