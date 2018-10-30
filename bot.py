import requests


TOKEN = "640743547:AAHWPuEhr5twym7IkhAQ28ciGRpSRwDG4Vc"
T_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def sendMessage(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(T_URL + 'sendMessage', data=params)
    return response


sendMessage('343217412', 'Hello')
