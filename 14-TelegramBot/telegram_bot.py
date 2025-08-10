import telebot
from telebot import types


bot = telebot.TeleBot("Token", parse_mode=None)



markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('تست 1')
itembtn2 = types.KeyboardButton('تست 2')
itembtn3 = types.KeyboardButton('تست 3')
markup.add(itembtn1, itembtn2, itembtn3)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "سلام دوست عزیز به ربات من خوش اومدی چه کمکی از دستم بر میاد؟😉")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "سلام":
	    bot.send_message(message.chat.id, "سلام خوبی؟ چه خبرا؟")
	elif message.text == "خوبی":
	    bot.send_message(message.chat.id, "من که خوبم عزیزم ، امیدوارم تو هم خوب باشی")
	else:
	    bot.send_message(message.chat.id, "نمیفهمم چی میگی .... ",reply_markup=markup)



bot.infinity_polling()