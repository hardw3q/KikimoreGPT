import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up OpenAI API key
openai.api_key = "TOKEN"

# Set up Telegram Bot
updater = Updater(token="TOKEN", use_context=True)
dispatcher = updater.dispatcher

def chatbot(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Response: ' + message,
        max_tokens=4000,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

chat_handler = MessageHandler(Filters.text, chatbot)
dispatcher.add_handler(chat_handler)

updater.start_polling()
