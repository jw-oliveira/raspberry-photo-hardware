import time
import picamera
from telegram_sender import enviar_imagem
from datetime import datetime


def capture_image(image_name):
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}.jpg')


while True:
    label = input(str())
    caption = f'Pedido: {label[0:5]} \nCaixa: {label[-2:]}'
    print(f'Etiqueta Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    capture_image(label)
    print(f'Imagem Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    enviar_imagem(f'/home/jorge/Pictures/camera_test/{label}.jpg', caption)
    print(f'Imagem enviada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
