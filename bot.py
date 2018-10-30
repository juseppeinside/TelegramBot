bot = telebot.TeleBot(TOKEN)
upd = bot.get_updates()
last_upd = upd[-1]


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message.text)
    if message.text == "ты тупой":
        bot.send_message(message.chat.id, "Сори, но мираж не играю")
    elif message.text == "говно из жопы":
        bot.send_message(message.chat.id, "шоколад")
    else:
        bot.send_message(message.chat.id, "Полный крииинж")



bot.polling(none_stop=True,  interval=0)
