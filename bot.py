import telebot
import random
import time
import threading
from telebot.types import ReactionTypeEmoji
from flask import Flask

# Dummy web server for Render health check
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive and running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# Start web server in background
t = threading.Thread(target=run_web)
t.start()

# Aapke 5 bots ke tokens
TOKENS = [
    '8776109160:AAELNteGzrI7htw63cRldsgGCBLCqNoTMac', 
    '8799593266:AAF14cEtHVJTyd93fSPg6DKk7wttmVR6TSU', 
    '8685137191:AAHhMSkQBGCxDgbsB7LpOouoZJV8aZQD46U', 
    '8536769973:AAH6SUq53RJD5qYQY49WoZa8L45ZdZiZKrk', 
    '8685196226:AAG4DPZ9PKSvNoL8BOrO0tZbHddyicVuOng'  
]

main_bot = telebot.TeleBot(TOKENS[0])

@main_bot.channel_post_handler(func=lambda message: True)
def auto_react_multiple(message):
    emoji_list = ['🔥', '❤️', '👍', '🎉', '🤩', '⚡️']
    for token in TOKENS:
        try:
            temp_bot = telebot.TeleBot(token)
            chosen_emoji = random.choice(emoji_list)
            reactions = [ReactionTypeEmoji(chosen_emoji)]
            temp_bot.set_message_reaction(message.chat.id, message.message_id, reactions)
            time.sleep(1) 
        except Exception as e:
            pass

while True:
    try:
        main_bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        time.sleep(5)
