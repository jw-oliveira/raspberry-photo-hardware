import time
import picamera
from telegram_sender import enviar_imagem


def capture_image(image_name):
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}.jpg')


while True:
    label = input(str())
    print('Etiqueta Capturada')
    capture_image(label)
    print('Imagem Capturada')
    enviar_imagem(f'/home/jorge/Pictures/camera_test/{label}.jpg', label)
    print('Imagem enviada')
