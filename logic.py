# Задание 2 - Импортируй нужные классы

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def text(self):
        return self.__text


    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        markup = InlineKeyboardMarkup()

        for i, question in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(question, callback_data='cb_correct'))
            else:
                markup.add(InlineKeyboardButton(question, callback_data='cb_wrong'))

        return markup
    def count_self(self):
        return len(self.options)



# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
