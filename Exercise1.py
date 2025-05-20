# Creating a bot using the Telegram Bot API (BotFather)
# Installing the package python-telegram-bot:
! pip install python-telegram-bot

# Importing essential libraries
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Configuring logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# When received the command /start, the bot answers "I'm a bot, please talk to me!"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

# Initial configuration of the bot
if __name__ == '__main__':

    # Changing the 'TOKEN' for the token given by BotFather
    application = ApplicationBuilder().token('TOKEN').build()

    # Setting a Handler to answer the command /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Runs the bot until the CTRL + C is typed
    application.run_polling()

# Essential libraries for running the code

from typing import Final
from telegram import Update
from telegram.ext import *
import logging
import responses
import nest_asyncio

# Firstly, insert the token given by BotFather
TOKEN = 'INSERT YOUR TOKEN HERE'

# Creating the logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Inicializando o bot...')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Olá! Sou um robô!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Em que posso te ajudar?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Esse é um comando personalizado.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text = str(update.message.text).lower()
  logging.info(f'Usuário ({update.message.chat.id}) disse: {text}')

  # Bot's answer (it is what the user said)

  await update.message.reply_text(text)


async def error(update, context):
  logging.error(f'Update ({update}) caused error: {context.error}')

def main():

  # Creates an application with the used token

  application = Application.builder().token(TOKEN).build()


  # Commands

  application.add_handler(CommandHandler('start', start_command))
  application.add_handler(CommandHandler('help', help_command))
  application.add_handler(CommandHandler('custom', custom_command))

  # Messages

  application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

  # Running the bot

  # We need to use nest_asyncio to be able to run the bot on Google Colab

  nest_asyncio.apply()

  application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

