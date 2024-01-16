import time
import picamera
from telegram_sender import enviar_imagem
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def capture_image(image_name):
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}.jpg')


while True:
    label = input(str())
    print(f'Etiqueta Capturada - {now}')
    capture_image(label)
    print(f'Imagem Capturada - {now}')
    enviar_imagem(f'/home/jorge/Pictures/camera_test/{label}.jpg', label)
    print(f'Imagem enviada - {now}')
