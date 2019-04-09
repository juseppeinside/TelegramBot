import requests
import yandex_translate
import json

BOT_TOKEN = "******************************************"
T_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

def getUpdates():
    response = requests.get(T_URL + 'getUpdates')
    return response.json()

def lastUpdate(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def getChatId(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def sendMessage(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(T_URL + 'sendMessage', data = params)
    return response

def main():

    update_id = lastUpdate(getUpdates())['update_id']
    while True:
        if update_id == lastUpdate(getUpdates())['update_id']:
            from yandex_translate import YandexTranslate
            translate = YandexTranslate(
                'trnsl.1.1.20181221T225719Z.e3a1a909c9a77883.918af8cc684b8477f891022c74cccc76ef2709b5')
            c = (lastUpdate(getUpdates())['message']['text'])
            w = translate.translate(c,'ru-en')

            trans = w['text']
            sendMessage(getChatId(lastUpdate(getUpdates())), trans)
            update_id += 1
    sleep(1)


if __name__ == '__main__':
    main()