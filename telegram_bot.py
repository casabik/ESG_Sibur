import telebot
from requests import get

bot = telebot.TeleBot('6970949344:AAEl0nBgUZtA4XFwubYYrj8bQPlm_-fOqiQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, Я могу помочь тебе найти комментарий в группе Вконтакте паблика Сибур! Напиши любой текст, и я найду подходящий комментарий!")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    query = message.text  
    answer = get("http://127.0.0.1:8000/get_comments", params = {'user_text': query})
    answer = answer.json()
    if answer['message'] == "Not found":
        bot.send_message(message.chat.id, "К сожалению таких комментариев нет(")
    else:
        comments = answer['comments']
        for comment in comments:
            bot.send_message(message.chat.id, f"Id комментария - {comment['comment_id']}\nperson_id - {comment['person_id']}\nДата - {comment['date']}\nТекст комментария - {comment['text']}\nId поста - {comment['post_id']}\nКоличество лайков - {comment['likes']}")
bot.infinity_polling(none_stop=True)
