#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from mako.template import Template

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    bot_name = context.bot.first_name
    html = Template("Hello! My name is <b>" + bot_name + "</b>.\n\nType /greet and i will greet you.").render()
    update.message.reply_html(html)


def greet(update: Update, context: CallbackContext) -> None:
    name = update.message.chat.first_name
    try:
        html = Template("Hello <b>" + name + "</b>!").render()
        update.message.reply_html(html)
    except:
        html = "Hey, be careful with your payload."
        update.message.reply_html(html)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("***REMOVED***")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("greet", greet))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
