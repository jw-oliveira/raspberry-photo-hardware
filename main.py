import time
import picamera


def capture_image(image_name):
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}')


label = input(str())
capture_image(label)
