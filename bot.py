import telebot
from requests import get

bot = telebot.TeleBot('6385936905:AAFXH76zAcS5E2jtroVTSfNNJESi43L0TRw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, добро пожаловать в Свободный! Напиши имя любого человека из города, и я о нем тебе расскажу все что знаю")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    s = message.text 
    query = s
    answer = get("http://localhost:8000/user?query=" + query).json()
    bot.send_message(message.from_user.id, answer)

bot.infinity_polling(none_stop=True)
