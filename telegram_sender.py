import requests
from telegram import Bot
from telegram import InputFile

apiToken = '6806885063:AAHm3Mwd_-whmTsfNEt1jZaJqMgovu-VbN8'

def telegram_message(message):
    chat_id = '-4162147141'
    api_url = f'https://api.telegram.org/bot{apiToken}/sendPhoto'

    try:
        requests.post(api_url, json={'chat_id': chat_id, 'text': message})
    except Exception as error:
        print(error)
        

def enviar_imagem(file_path):
    body = {
        'chat_id': '-4162147141',
    }
    files = {
        'photo': open(file_path, 'rb')
    }
    r = requests.post('https://api.telegram.org/bot{}/sendPhoto'.format(
    apiToken), data=body, files=files)
    if r.status_code >= 400:
        print('Houve um erro ao enviar mensagem. Detalhe: {}'.format(r.text))
    else:
        print('Mensagem enviada com sucesso.')

