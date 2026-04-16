import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Castle Bot is running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "Webhook Done"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "أهلاً بك في بوت قلعة 🏰")

if __name__ == "__main__":
    bot.set_webhook(url=f"https://castle-m0f8.onrender.com/{TOKEN}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
