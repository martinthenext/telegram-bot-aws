# Telegram bot boilerplate for AWS

Minimum LOC in Python you can deploy to AWS and get a bot to respond "Hello world" to a message. 

`bot.py` - AWS Lambda event handler bot boilerplate. No frameworks, no unreasonable dependencies.

Grab the code, easily deploy it on AWS to handle your bot's requests, and your bot is all set. Deployment is based on [python-λ](https://github.com/nficano/python-lambda). If you want flexibility to deploy your bot on different cloud platforms, check out [this excellent guide](https://hackernoon.com/serverless-telegram-bot-on-aws-lambda-851204d4236c) on using the [Serverless framework](https://serverless.com) instead.

### Requirements

- [Access key id and secret](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for your AWS account 
- An access token for your Telegram bot you received from [Botfather](https://core.telegram.org/bots#6-botfather)
- Virtualenvwraper

### Deployment

Set up [python-λ](https://github.com/nficano/python-lambda/blob/master/README.rst#getting-started) environment in this repository you cloned:

```bash
$ mkvirtualenv bot
(bot) $ pip install python-lambda
(bot) $ pip install requests
```

Edit `config.yaml` file to specify AWS and Telegram keys

Deploy:

```bash
(bot) $ lambda deploy
```

> The deploy script will evaluate your virtualenv and identify your project dependencies. It will package these up along with your handler function to a zip file that it then uploads to AWS Lambda.

### Setting up API Gateway

Should be similar to [this](https://github.com/nficano/python-lambda/blob/master/README.rst#wiring-to-an-api-endpoint) and also done automatically.

### Setting up webhooks

Should be done automatically as well.

### 







