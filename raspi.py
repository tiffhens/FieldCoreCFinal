import RPi.GPIO as GPIO

SENSOR_PIN1  = 22
SENSOR_PIN2  = 27

chan_list = [22,27]

class Raspi(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(chan_list, GPIO.IN)
    
    def read_sensor(self):
        sensor1 = GPIO.input(chan_list[0])
        sensor2 = GPIO.input(chan_list[1])
        return [sensor1,sensor2]

#  def change_led(self, value):
#    GPIO.output(LED_PIN, value)