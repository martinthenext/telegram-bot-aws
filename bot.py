import os
import json
import requests


SEND_MSG_URL = 'https://api.telegram.org/bot{}/sendMessage'


def handle(event, context):
    data = json.loads(event['body'])
    chat_id = data['message']['chat']['id']

    response = {'text': 'Hello, world', 'chat_id': chat_id}
    url = SEND_MSG_URL.format(os.environ['TELEGRAM_TOKEN']
    requests.post(sendmsg_url, response)

    return {'statusCode': 200}

