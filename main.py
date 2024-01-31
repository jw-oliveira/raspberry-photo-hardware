import picamera
import base64
import io
import json
from datetime import datetime

camera = picamera.PiCamera()


def capture_image(image_name):
    camera.resolution = (1920, 1080)
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', quality=10)
    image_binary = stream.getvalue()
    base64_data = base64.b64encode(image_binary).decode('utf-8')

    value = {
        "order_id": image_name[0:6],
        "base64_data": base64_data
    }

    return json.dumps(value)


while True:
    image_name_input = input(str())
    print(capture_image(image_name_input))
    print(f'Imagem Capturada - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
