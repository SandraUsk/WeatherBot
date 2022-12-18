import telebot
from telebot import types
from data import token
from data import msk_id
from data import spb_id
from data import get_weather
from data import get_suntime


bot = telebot.TeleBot(token)

class User:
    def __init__(self, city):
        self.city_id = city

user = User(msk_id)

@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Москва")
    item2 = types.KeyboardButton("Санкт-Петербург")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Привет! Откуда вы? Выберите вариант или напишите сами (на английском!)', reply_markup=markup)

@bot.message_handler(commands = ['help'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("/start")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Этот бот показывает погоду и время восхода и захода солнца. Для начала работы нажмите /start и следуйте инструкциям ;)', reply_markup=markup)

@bot.message_handler(content_types = 'text')
def answers(message):
    try:
        if message.text == "Погода":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Погода")
            item2 = types.KeyboardButton("Восход и заход солнца")
            item3 = types.KeyboardButton("Сменить город")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, get_weather(user.city_id), reply_markup=markup)
        elif message.text == "Восход и заход солнца":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Погода")
            item2 = types.KeyboardButton("Восход и заход солнца")
            item3 = types.KeyboardButton("Сменить город")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, get_suntime(user.city_id), reply_markup=markup)
        elif message.text == "Сменить город":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Москва")
            item2 = types.KeyboardButton("Санкт-Петербург")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, 'Привет! Откуда вы? Выберите вариант или напишите сами (на английском!)', reply_markup=markup)
        elif message.text == "Москва":
            user.city_id = msk_id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Погода")
            item2 = types.KeyboardButton("Восход и заход солнца")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=markup)
        elif message.text == "Санкт-Петербург":
            user.city_id = spb_id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Погода")
            item2 = types.KeyboardButton("Восход и заход солнца")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=markup)
        else:
            user.city_id = "q=" + message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Погода")
            item2 = types.KeyboardButton("Восход и заход солнца")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте другой город или проверьте написание')


bot.polling(none_stop = True, interval = 0)
