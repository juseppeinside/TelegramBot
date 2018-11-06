import requests
from time import sleep


BOT_TOKEN = ’your telegram bots token'
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
            sendMessage(getChatId(lastUpdate(getUpdates())), 'test')
            update_id += 1
            print(lastUpdate(getUpdates())['message']['text'])
    sleep(1)




if __name__ == '__main__':
    main()
