import time
import picamera
from telegram_sender import send_message


def capture_image(image_name):
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}.jpg')


label = input(str())
capture_image(label)
send_message('test',f'/home/jorge/Pictures/camera_test/{label}.jpg')
