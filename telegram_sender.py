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

# Exemplo de uso sem imagem
mensagem_sem_imagem = "Olá, esta é uma mensagem sem imagem!"
send_message(mensagem_sem_imagem)

# Exemplo de uso com imagem
caminho_da_imagem = 'CAMINHO_DA_IMAGEM'  # Substitua pelo caminho real da imagem
mensagem_com_imagem = "Olá, esta é uma mensagem com imagem!"
send_message(mensagem_com_imagem, caminho_da_imagem)