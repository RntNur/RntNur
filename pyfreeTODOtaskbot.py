import random

from random import choice

import telebot

token = "5767843786:AAHdJlOdcS8PTR1dCczSna47xC6jcVD92lU"
bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']




HELP = '''
Список доступных команд:
/show  - напечать все задачи на заданную дату
/todo - добавить задачу
/random - добавить на сегодня случайную задачу
/help - Вывести список команд
/add  - Добавить задачу
'''
todos = {}
def add_todo(date, task):
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in todos:
        text = date.upper() + "\n"
        for task in todos[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "ЗАдача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')

bot.polling(none_stop=True)
