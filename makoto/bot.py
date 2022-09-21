#!/usr/bin/env python

# <u_dont_need_read_this_lol>

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
    except Exception as e:
        txt = str(e)
        update.message.reply_text(txt)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("[BOT_TOKEN]")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("greet", greet))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
