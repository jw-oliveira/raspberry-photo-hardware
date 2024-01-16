import requests
from telegram import Bot
from telegram import InputFile

apiToken = '6806885063:AAHm3Mwd_-whmTsfNEt1jZaJqMgovu-VbN8'
chatId = '-4162147141'


def enviar_imagem(file_path, caption):
    body = {
        'chat_id': chatId,
        'caption': caption
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

