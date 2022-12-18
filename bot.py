import telebot
from telebot import types
from data import token
from data import msk_id
from data import get_weather
from data import get_suntime


bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Погода")
    item2 = types.KeyboardButton("Восход и заход солнца")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Привет! Что вы хотите узнать? :)', reply_markup=markup)
@bot.message_handler(content_types = 'text')
def message_reply(message):
    if message.text == "Погода":
        bot.send_message(message.chat.id, get_weather(msk_id))
    if message.text == "Восход и заход солнца":
        bot.send_message(message.chat.id,get_suntime(msk_id))

bot.polling(none_stop = True, interval = 0)
