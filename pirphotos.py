import RPi.GPIO as GPIO
import time
import datetime
import picamera

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S.jpg")

sensor = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

cam = picamera.PiCamera()

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
        if new_state == "HIGH":
            print("Take a photo!")
            cam.resolution = (800, 600)
            cam.start_preview()
            cam.capture(get_file_name())


