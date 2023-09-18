# import telebot

# 

# bot = telebot.TeleBot('Bu yerga BotFather dan olgan tokeningizni qoying')


# @bot.message_handler(commands=['start'])
# def start(message):
#     ismi = str(message.from_user.first_name)
#     bot.send_message(message.from_user.id, text=f"Salom {ismi} yaxshimisiz?")
#     #Boshqa kodlaringizni yozishingiz mumkin
    
    
# if __name__ == '__main__':
#     bot.polling(none_stop= True) # bu botimiz ochib qolmasligi uchun!
import telebot

"""Telegramda @azamatcoders kanaliga va github profilimga obuna bo'lib qo'ying"""

# Bot tokenini o'zgartiring
bot = telebot.TeleBot('Token')
ADMINS = 2003490906,2003490906


# Foydalanuvchi ma'lumotlarini saqlayish uchun lug'at (dict)
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    bot.send_message(chat_id, "Salom! Iltimos, ismingizni yozing:")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    chat_id = message.chat.id
    user_data[chat_id]['name'] = message.text
    
    bot.send_message(chat_id, "Familiyangizni yozing:")
    bot.register_next_step_handler(message, get_lastname)

def get_lastname(message):
    chat_id = message.chat.id
    user_data[chat_id]['lastname'] = message.text
    
    bot.send_message(chat_id, "Yoshingizni yozing:")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    chat_id = message.chat.id
    user_data[chat_id]['age'] = message.text
    bot.send_message(chat_id, "Manzilingizni yozing:")
    bot.register_next_step_handler(message, get_address)
 

def get_address(message):
    chat_id = message.chat.id
    user_data[chat_id]['address'] = message.text
    
    bot.send_message(chat_id, "Kasbingizni yozing:")
    bot.register_next_step_handler(message, get_occupation)

def get_occupation(message):
    chat_id = message.chat.id
    user_data[chat_id]['occupation'] = message.text
    
    # Foydalanuvchi ma'lumotlarini ko'rsatish
    user_info = user_data[chat_id]
    response = f"👱‍♂️ Ism: {user_info['name']}\n🥈 Familiya: {user_info['lastname']}\n🚀 Yosh: {user_info['age']}\n📍 Manzil: {user_info['address']}\n🎓 Kasb: {user_info['occupation']}"
    for admin in ADMINS:
        bot.send_message(chat_id=admin, text=response)
        
    bot.send_message(chat_id=message.chat.id,text="ADMIN larga xabar yuborildi ✅")


if __name__ == '__main__':
    bot.polling(none_stop=True)
