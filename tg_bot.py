import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai_secret_manager
import openai
openai.api_key = "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"
model_engine = "text-davinci-002"

# Initialize previous response to None
prev_response = None

def generate_answer(prompt, context):
    # Use previous response as context if available
    if context is not None:
        prompt = context + "\n" + prompt
    prompt = "Answer this question: " + prompt + "\nAnswer:"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
    message = completions.choices[0].text.strip()
    return message

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я чат-бот, который может отвечать на вопросы. Просто задайте мне вопрос и я постараюсь дать вам наиболее подходящий ответ!")

def answer_question(update, context):
    global prev_response
    question = update.message.text
    try:
        response = generate_answer(question, prev_response)
    except Exception as e:
        response = str(e)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    prev_response = response

if __name__ == "__main__":
    # Create Updater object and attach dispatcher to it
    updater = Updater(token='5488163951:AAHiDGVOzGat8XaxW2HR71tbTaxtZZpOMMo', use_context=True)
    dispatcher = updater.dispatcher

    # Add command handler to dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add message handler to dispatcher
    message_handler = MessageHandler(Filters.text & ~Filters.command, answer_question)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
