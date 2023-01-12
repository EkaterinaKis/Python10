import telebot
import requests


bot = telebot.TeleBot('place for your token')

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


@bot.message_handler(commands=['start'])
def first_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)       #ресайз помогает подстраивать клавиатуру под размер открытого окна телеграм
    markup.row('USD', 'EUR')
    markup.row('CNY', 'KZT')
    markup.row('GBP', 'JPY')
    msg = bot.send_message(
        message.chat.id, "Курс какой валюты вы хотите узнать", reply_markup=markup)
    bot.register_next_step_handler(msg, choose_currency)


def choose_currency(message):
    try:
        if message.text == 'USD':
            bot.send_message(message.chat.id, res['Valute']['USD']['Value'])
            bot.register_next_step_handler(message, choose_currency)
        elif message.text == 'EUR':
            bot.send_message(message.chat.id, res['Valute']['EUR']['Value'])
            bot.register_next_step_handler(message, choose_currency)
        elif message.text == 'CNY':
            bot.send_message(message.chat.id, res['Valute']['CNY']['Value'])
            bot.register_next_step_handler(message, choose_currency)
        elif message.text == 'KZT':
            bot.send_message(message.chat.id, res['Valute']['KZT']['Value'])
            bot.register_next_step_handler(message, choose_currency)
        elif message.text == 'GBP':
            bot.send_message(message.chat.id, res['Valute']['GBP']['Value'])
            bot.register_next_step_handler(message, choose_currency)
        elif message.text == 'JPY':
            bot.send_message(message.chat.id, res['Valute']['JPY']['Value'])
            bot.register_next_step_handler(message, choose_currency)
    except Exception:
        bot.send_message(message.chat.id, 'Введите корректные данные')
        bot.register_next_step_handler(message, choose_currency)


bot.polling()
