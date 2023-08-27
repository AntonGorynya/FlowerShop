import telegram
from textwrap import dedent


def send_notification(bot, chat_id, message):
    bot.send_message(chat_id=chat_id, text=dedent(message))
