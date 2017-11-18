"""
Telegram bot boilerplate for AWS in Python. The bot responds 'Hello, world'
to any message.

"""
import os
import json
import requests


SEND_MSG_URL = 'https://api.telegram.org/bot{}/sendMessage'


def handle(event, context):
    """ This function gets invoked when Lambda is called.

    """
    data = json.loads(event['body'])
    chat_id = data['message']['chat']['id']

    response = {'text': 'Hello, world', 'chat_id': chat_id}
    sendmsg_url = SEND_MSG_URL.format(os.environ['TELEGRAM_TOKEN'])
    requests.post(sendmsg_url, response)

    return {'statusCode': 200}

