import telebot
import config
from telebot import types
import random

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Photo\sticker.webp', 'rb')
    if message.from_user.first_name != None and message.from_user.last_name != None:
        helloistvie = f'Добро Пожаловать, {message.from_user.first_name} {message.from_user.last_name}!'
    elif message.from_user.first_name == None:
        helloistvie = f'Добро Пожаловать, {message.from_user.last_name}!'
    else:
        helloistvie = f'Добро Пожаловать, {message.from_user.first_name}!'


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Тест на гея")
    item2 = types.KeyboardButton("Я гущин")
    markup.add(item1, item2)

    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, helloistvie, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def say(message):
    if message.chat.type == "private":
        if message.text == "Я гущин":
            bot.send_message(message.chat.id, "Поздравляю, ты гей на 100%")
        elif message.text == "Тест на гея":
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("Я из Гущиных", callback_data='guschc')
            item2 = types.InlineKeyboardButton("Я - не Гущин (нормальный)", callback_data='norm')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Выбери один из вариантов ниже.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def InlineKeyboardMarkup1(call):
    try:
        a = [(0, 49), (50, 100)]
        if call.message:
            if call.data == 'guschc':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Поздравляю, ты гей на 100%", reply_markup=None)
            elif call.data == 'norm':
                procent = a[random.randint(0, 1)]
                procent = random.randint(procent[0], procent[1])
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f'Поздравляю, ты гей на {procent}%', reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ХЕХЕХЕХЕХЕ")
    except:
        pass


bot.polling(none_stop=True)
