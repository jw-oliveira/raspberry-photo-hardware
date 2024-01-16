import requests
from telegram import Bot
from telegram import InputFile

apiToken = '6806885063:AAHm3Mwd_-whmTsfNEt1jZaJqMgovu-VbN8'
chat_id = '-4162147141'


def send_message(message, imagem_path=None):
    try:
        bot = Bot(apiToken)

        if imagem_path:
            photo = InputFile(imagem_path)
            bot.send_photo(chat_id=chat_id, photo=photo, caption=message)
        else:
            bot.send_message(chat_id=chat_id, text=message)

        print("Mensagem enviada com sucesso para o Telegram!")
    except Exception as error:
        print(f"Erro ao enviar mensagem para o Telegram: {error}")
