import os
import telebot
from flask import Flask
import threading

# گرفتن توکن از Secrets
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# راه‌اندازی وب‌سرور برای UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "ربات آنلاین است ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

# دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من یه ربات ساده‌ام. هر متنی بفرستی، همونو برمی‌گردونم. 😊")

# پاسخ به تمام پیام‌های متنی
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# اجرای همزمان وب‌سرور و ربات
if __name__ == "__main__":
    threading.Thread(target=run).start()
    print("ربات روشن شد... 🚀")
    bot.infinity_polling()
