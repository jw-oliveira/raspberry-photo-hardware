import time
import picamera
import base64
import io
from telegram_sender import enviar_imagem
from datetime import datetime


def capture_image():
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        # camera.capture(f'/home/jorge/Pictures/camera_test/{image_name}.jpg', quality=10)
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg', quality=10)
        image_binary = stream.getvalue()
        base64_data = base64.b64encode(image_binary).decode('utf-8')
        return base64_data


while True:
    #label = input(str())
    #caption = f'Pedido: {label[0:6]} \nCaixa: {label[-2:]}'
    #print(f'Etiqueta Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(capture_image())
    print(f'Imagem Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    # enviar_imagem(f'/home/jorge/Pictures/camera_test/{label}.jpg', caption)
    # print(f'Imagem enviada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
