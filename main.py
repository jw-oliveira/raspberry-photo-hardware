import time
import picamera
import base64
import io
from telegram_sender import enviar_imagem
from datetime import datetime


def capture_image():
    with picamera.PiCamera() as camera:
        time.sleep(0.5)
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg', quality=10)
        image_binary = stream.getvalue()
        base64_data = base64.b64encode(image_binary).decode('utf-8')
        return base64_data


print(capture_image())
print(f'Imagem Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

