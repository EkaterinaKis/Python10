import telebot
import requests


bot = telebot.TeleBot("place for your token")

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


@bot.message_handler(commands=['start'])
def first_message(message):
    msg = bot.send_message(
        message.chat.id, "Курс какой валюты вы хотите узнать: USD, EUR, CNY, KZT, GBP, JPY?")
    bot.register_next_step_handler(msg, choose_currency)


def choose_currency(message):
    try:
        if message.text == 'USD':
            bot.send_message(message.chat.id, res['Valute']['USD']['Value'])
        elif message.text == 'EUR':
            bot.send_message(message.chat.id, res['Valute']['EUR']['Value'])
        elif message.text == 'CNY':
            bot.send_message(message.chat.id, res['Valute']['CNY']['Value'])
        elif message.text == 'KZT':
            bot.send_message(message.chat.id, res['Valute']['KZT']['Value'])
        elif message.text == 'GBP':
            bot.send_message(message.chat.id, res['Valute']['GBP']['Value'])
        elif message.text == 'JPY':
            bot.send_message(message.chat.id, res['Valute']['JPY']['Value'])  
    except Exception:
        bot.send_message(message.chat.id, 'Введите корректные данные')


bot.polling()
