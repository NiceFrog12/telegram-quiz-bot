import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from logic import quiz_questions

bot = telebot.TeleBot(token)

user_responses = {} 
# Задание 8 - создай словарь points для сохранения количества очков пользователя

bot = telebot.TeleBot(token)

score = {}

def send_question(chat_id):
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        # Задание 9 - добавь очки пользователю за правильный ответ
        score[call.message.chat.id] += 1
    elif call.data == "cb_wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
      
    #i made this myself to disable the button after 1 use so that you can't get infinite points
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)


    # Задание 5 - реализуй счетчик вопросов
    user_responses[call.message.chat.id] += 1
    # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос
    if user_responses[call.message.chat.id] < len(quiz_questions):
        send_question(call.message.chat.id)
    else:
        bot.send_message(call.message.chat.id, f"There are no more questions. Your end score is {score[call.message.chat.id]}")


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        score[message.chat.id] = 0 
        send_question(message.chat.id)

@bot.message_handler(commands=['score'])
def scorecount(message):
    bot.send_message(message.chat.id, f"Your score currently is {score.get(message.chat.id, 0)}")


bot.infinity_polling()
