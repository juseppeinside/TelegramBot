# -*- coding: utf-8 -*-
import telebot

TOKEN = "640743547:AAHWPuEhr5twym7IkhAQ28ciGRpSRwDG4Vc"
bot = telebot.TeleBot(TOKEN)
upd = bot.get_updates()
last_upd = upd[-1]


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message.text)
    if message.text == "1":
        bot.send_message(message.chat.id, "Сори, но мираж не играю")
    elif message.text == "2":
        bot.send_message(message.chat.id, "Шоколад")
    else:
        bot.send_message(message.chat.id, "Полный крииинж")



bot.polling(none_stop=True,  interval=0)
