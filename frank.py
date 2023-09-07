import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import pymysql.cursors
from datetime import datetime


token = ""
bot= telebot.TeleBot(token)
restaurants = ["РОЖДЕСТВЕНКА, 5/7" , "ТИМУРА ФРУНЗЕ, 22" , "МЯСНИЦКАЯ, 24" , "ПЯТНИЦКАЯ, 10" , "НОВЫЙ АРБАТ, 17" , "КАМЕРГЕРСКИЙ ПЕР., 6" , "УСАЧЕВА, 26" , "ТРК ПАВЕЛЕЦКАЯ ПЛАЗА" , "БОЛЬШАЯ НОВОДМИТРОВСКАЯ, 36 С14" , "ЛЕСНАЯ УЛ., 20, СТ. 6"]
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = types.KeyboardButton("Забронировать столик")
    btn2 = types.KeyboardButton("МЕНЮ 🥩")
    btn3 = types.KeyboardButton("НАШИ РЕСТОРАНЫ🍴")
    btn4 = types.KeyboardButton("НАШ САЙТ🌐")
    btn5 = types.KeyboardButton("🔥АКЦИИ🔥")
    btn6 = types.KeyboardButton("Наши соц. сети")
    markup.add(btn1)
    markup.add(btn2,btn3)
    markup.add(btn4,btn5)
    markup.add(btn6)

    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}! 👋 \nВас приветствует телеграм бот ресторана Frank By Баста Москва!".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Выберите желаемую функцию!", reply_markup=markup)

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn1 = types.KeyboardButton("Забронировать столик")
    btn2 = types.KeyboardButton("МЕНЮ 🥩")
    btn3 = types.KeyboardButton("НАШИ РЕСТОРАНЫ🍴")
    btn4 = types.KeyboardButton("НАШ САЙТ🌐")
    btn5 = types.KeyboardButton("🔥АКЦИИ🔥")
    btn6 = types.KeyboardButton("Наши соц. сети")
    markup.add(btn1)
    markup.add(btn2,btn3)
    markup.add(btn4,btn5)
    markup.add(btn6)
    bot.send_message(message.chat.id,text="Вы вернулись в главное меню! Выберите желаемую функцию.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Забронировать столик"):
        bron(message)
    
    elif (message.text == "МЕНЮ 🥩"):
        markup = InlineKeyboardMarkup()
        telebot.types.ReplyKeyboardRemove
        
        markup.add(InlineKeyboardButton(text='Вернуться', callback_data='rollback'))
        menuosn = InlineKeyboardButton(text='Основное меню', url = 'https://frankmeat.ru/menu')
        menubar = InlineKeyboardButton(text='Барная карта', url = 'https://frankmeat.ru/menu-bar')
        markup.add(menuosn,menubar)
        bot.send_message(message.chat.id, text="Вы можете ознакомиться с нашим меню, нажав на кнопки ниже.",reply_markup=markup)
    elif (message.text == "НАШИ РЕСТОРАНЫ🍴"):
        markup = InlineKeyboardMarkup()
        telebot.types.ReplyKeyboardRemove
        markup.add(InlineKeyboardButton(text='Вернуться', callback_data='rollback'))
        bot.send_message(message.chat.id, text ="РОЖДЕСТВЕНКА, 5/7\n🕰️ Вс-чт 12.00—01.00\n🕰️ Пт-сб 12.00—03.00\n\nТИМУРА ФРУНЗЕ, 22\n🕰️ Пн-Вс 12:00-23:00\n\nМЯСНИЦКАЯ, 24\n🕰️ Вс-чт 12.00—01.00\n🕰️ Пт-сб 12.00—03.00\n\nПЯТНИЦКАЯ, 10\n🕰️ Вс-ср 12.00—00.00\n🕰️ Чт 12.00—01.00\n🕰️ Пт-сб 12.00—03.00\n\nНОВЫЙ АРБАТ, 17\n🕰️ Вс-чт 12.00—01.00\n🕰️ Пт-сб 12.00—03.00\n\nКАМЕРГЕРСКИЙ ПЕР., 6\n🕰️ Вс-чт 12.00—00.00\n🕰️ Пт-сб 12.00—03.00\n\nУСАЧЕВА, 26\n🕰️ Вс-чт 12.00—23.00\n🕰️ Пт-сб 12.00—00.00\n\nТРК ПАВЕЛЕЦКАЯ ПЛАЗА\n🕰️ Пн-вс 10.00—23.00\n\nБОЛЬШАЯ НОВОДМИТРОВСКАЯ, 36 С14\n🕰️ Вс-чт 12.00—00.00\n🕰️ Пт-сб 12.00—03.00\n\nЛЕСНАЯ УЛ., 20, СТ. 6\n🕰️ Вс-чт 12.00—01.00\n🕰️ Пт-сб 12.00—03.00 ",reply_markup=markup)
    elif (message.text == "НАШ САЙТ🌐"):
        markup = InlineKeyboardMarkup()
        telebot.types.ReplyKeyboardRemove
        markup.add(InlineKeyboardButton(text='Вернуться', callback_data='rollback'))
        bot.send_message(message.chat.id, text = 'САЙТ🌐\nhttps://frankmeat.ru',reply_markup=markup)
    elif (message.text == "🔥АКЦИИ🔥"):
        markup = InlineKeyboardMarkup()
        telebot.types.ReplyKeyboardRemove
        markup.add(InlineKeyboardButton(text='Вернуться', callback_data='rollback'))
        bot.send_message(message.chat.id,text='🔥🔥🔥Наши акции🔥🔥🔥\n\n🎉🎉🎉В день рождения скидка 10%! Действует за 3 дня до дня рождения, в день рождения и ещё 3 дня после. Распространяется на всё основное меню и барную карту!\n\n🍳🍳🍳Сытные завтраки каждый день с 10:00 до 12:00!\n',reply_markup=markup)
    elif (message.text == "Наши соц. сети"):
        markup = InlineKeyboardMarkup()
        telebot.types.ReplyKeyboardRemove
        markup.add(InlineKeyboardButton(text='Вернуться', callback_data='rollback'))
        vk = InlineKeyboardButton(text='VK', url = 'https://vk.com/frankbybasta')
        tg = InlineKeyboardButton(text='Telegram', url = 'https://t.me/frankbybastamoscow')
        markup.add(vk,tg)
        bot.send_message(message.chat.id, text='Подписывайтесь на наши социальные сети и узнавайте первыми о новых акциях, мероприятиях и новостях!',reply_markup=markup)
def bron(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=2)
    caf1 = types.KeyboardButton("РОЖДЕСТВЕНКА, 5/7")
    caf2 = types.KeyboardButton("ТИМУРА ФРУНЗЕ, 22")
    caf3 = types.KeyboardButton("МЯСНИЦКАЯ, 24")
    caf4 = types.KeyboardButton("ПЯТНИЦКАЯ, 10")
    caf5 = types.KeyboardButton("НОВЫЙ АРБАТ, 17")
    caf6 = types.KeyboardButton("КАМЕРГЕРСКИЙ ПЕР., 6")
    caf7 = types.KeyboardButton("УСАЧЕВА, 26")
    caf8 = types.KeyboardButton("ТРК ПАВЕЛЕЦКАЯ ПЛАЗА")
    caf9 = types.KeyboardButton("БОЛЬШАЯ НОВОДМИТРОВСКАЯ, 36 С14")
    caf10 = types.KeyboardButton("ЛЕСНАЯ УЛ., 20, СТ. 6")
    markup.add(caf1,caf2,caf3,caf4,caf5,caf6,caf7,caf8,caf9,caf10)
    bot.send_video(message.chat.id,'https://adindex.ru/files2/news/2015_11/129800_1353.gif', None , caption='Выберие ресторан, в котором желаете забронировать столик.',reply_markup=markup)
    bot.register_next_step_handler(message,get_rest)
def get_rest(message):
    global rest
    rest = message.text.strip()
    if rest not in restaurants:
        bot.send_message(message.from_user.id, text = "Такого ресторана нет в списке!\nВведите название ресторана из списка ниже или нажмите на соответствующую кнопку!\n" + "\n".join(restaurants))
        bot.register_next_step_handler(message,get_rest)
    else:
        telebot.types.ReplyKeyboardRemove
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, 'Как к вам обращаться?',reply_markup=markup)
        bot.register_next_step_handler(message,ask_date)    


def ask_date(message):
    global name
    name = message.text.strip()
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
    bot.send_message(message.from_user.id, "Введите желаемую дату бронирования в формате ДД.ММ.ГГГГ, например 31.12.2022:",reply_markup=markup)
    bot.register_next_step_handler(message, check_date)

def check_date(message):
    global date

    try:
        date = datetime.strptime(message.text.strip(), "%d.%m.%Y").date()
    except ValueError:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Укажите дату в правильном формате!",reply_markup=markup)
        bot.register_next_step_handler(message, check_date)
        return

    if date < datetime.now().date():
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Вы указали прошедшую дату!",reply_markup=markup)
        bot.register_next_step_handler(message, check_date)
        return
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
    bot.send_message(message.from_user.id, "Введите желаемое время бронирования в формате ЧЧ:ММ, например 20:30:",reply_markup=markup)
    bot.register_next_step_handler(message, check_time)

def check_time(message):
    global time

    try:
        time = datetime.strptime(message.text.strip(), "%H:%M").time()
    except ValueError:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Укажите время в правильном формате!",reply_markup=markup)
        bot.register_next_step_handler(message, check_time)
        return

    now = datetime.now()
    chosen_datetime = datetime.combine(date, time)

    if chosen_datetime <= now:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Вы указали прошедшее время!",reply_markup=markup)
        bot.register_next_step_handler(message, check_time)
        return
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
    bot.send_message(message.from_user.id, "Введите количество человек:\nНе более 10 человек.",reply_markup=markup)
    bot.register_next_step_handler(message, check_people)

def check_people(message):
    global people

    try:
        people = int(message.text)
    except ValueError:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Введите количество человек в цифровом формате!",reply_markup=markup)
        bot.register_next_step_handler(message, check_people)
        return
    if people > 10:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Прервать процесс бронирования', callback_data='rollback'))
        bot.send_message(message.from_user.id, "Количество людей превышает допустимое, попробуйте снова!",reply_markup=markup)
        bot.register_next_step_handler(message, check_people)
        return
    markup = InlineKeyboardMarkup()
    conf = InlineKeyboardButton(text = 'Да', callback_data='confirmation')
    deny = InlineKeyboardButton(text='Нет', callback_data='deny')
    markup.add(conf,deny)
    bot.send_message(message.from_user.id,'Подтвердите бронирование. \nДа - Подтвердить бронирование\nНет - отменить процесс бронирования.',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call): 
    if call.data == "rollback":
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        bot.answer_callback_query(call.id)
        main_menu(call.message)
    elif call.data == "confirmation":
        connection = pymysql.connect(host='localhost',
        user='root',
        password='',
        database='frank',
        cursorclass=pymysql.cursors.DictCursor)
        with connection:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `booking`(`id`,`rest`,`name`,`date`,`time`,`amount`) VALUES ('',%s,%s,%s,%s,%s)"
                        cursor.execute(sql,(rest,name,date,time,people))
                        connection.commit()
        appl = "Вы успешно забронировали столик на " + str(date) + " " + str(time) + "\n" + "На " + str(people) + " человек" + " в ресторане по адресу " + str(rest) + "\n"
        bot.send_message(call.message.chat.id, appl)
        bot.answer_callback_query(call.id)
        main_menu(call.message)
    elif call.data == "deny":
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        bot.send_message(call.message.chat.id,"Бронирование отменено")
        bot.answer_callback_query(call.id)
        main_menu(call.message)
    elif call.data == "yes":
        bot.send_message(call.message.chat.id, text = "Вы успешно забронировали столик")
        bot.answer_callback_query(call.id)
        main_menu(call.message)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, text= "Бронирование отменено")
        bot.answer_callback_query(call.id)
        main_menu(call.message)
bot.infinity_polling()