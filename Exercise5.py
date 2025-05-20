# Integration of the Telegram bot to the logging

from typing import Final
from telegram import Update
from telegram.ext import *
import logging
import responses
import nest_asyncio
from getpass import getpass

# Token provided by BotFather
TOKEN = getpass()

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
  text = update.message.text
  input_ids = tokenizer(text, return_tensors="pt").input_ids.to("cuda")
  outputs = model.generate(input_ids, max_length=200, num_return_sequences=1)
  final_text = tokenizer.decode(outputs[0])
  y = final_text.split('\n')
  if len(y) > 0:
    final = y[0]
  else:
    x = final_text.split(". ")
    final = final_text.replace(x[-2], '')
    final = final.replace(". . . . . . ", '')
    final = final.replace(x[-1], '')

    final = final + " " + x[-2] + "."

  await update.message.reply_text(final)


async def error(update, context):
  logging.error(f'Update ({update}) caused error: {context.error}')

def main():

  # Creates an application for the token to be used

  application = Application.builder().token(TOKEN).build()


  # Commands

  application.add_handler(CommandHandler('start', start_command))
  application.add_handler(CommandHandler('help', help_command))
  application.add_handler(CommandHandler('custom', custom_command))

  # Messages

  application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

  # Running the bot

  nest_asyncio.apply()

  application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
