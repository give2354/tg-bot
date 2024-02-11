import sqlite3
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from logic import *

TOKEN = '6724957171:AAG0JoKEpeDncisdxlJYZxVoxUQRfhNvhSA'
bot = TeleBot(TOKEN)


def card_of_item(bot, message, row):
        
    info = f"""
Товар:   {row[1]}
Цвет:  {row[3]}
Цена:  {row[2]} рублей
"""
    try:

        with open(f'images/{row[4]}', 'rb') as photo:
             bot.send_photo(message.chat.id, photo)
    finally:
        bot.send_message(message.chat.id, info, reply_markup=gen_markup(row[0]))

def gen_markup(id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Добавить в корзину", callback_data=f'buy_{id}'))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("buy"):
        id = call.data[call.data.find("_")+1:]
        # Задание №2: отправь сообщение в чат "Товар добавлен в корзину"
        bot.send.message(call.message.chat.id, "товар добавлен в корзину")

@bot.message_handler(commands=['show_store'])
def show_store(message):
    # Задание №1: получи данные из бд
    res = manager.show_items()
    for row in res:
        card_of_item(bot, message, row)

if __name__ == '__main__':
    manager = StoreManager(DATABASE)
    bot.infinity_polling()