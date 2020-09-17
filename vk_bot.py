import datetime
import random
import os
import vk_api

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, text):
    random_id = random.random()
    vk.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random_id})


load_dotenv()
vk = vk_api.VkApi(token=os.environ.get("VK_BOT_API"))

longpoll = VkLongPoll(vk)

week_day_list = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
timetable_top_week = ["(8:30-10:05) Культура информациионого общества"
                      "\n(10:25-12:00) Математика(пр.)"
                      "\n (12:30-14:05) КУЛЬТУРА ИНФОРМАЦИОННОГО ОБЩЕСТВА",

                      "(8:30-10:05) ПСИХОЛОГ. МЕЖЛИЧНОСТ. ОТНОШЕНИЙ"
                      "\n(10:25-12:00) Физкультура"
                      "\n (12:30-14:05) СИСТЕМНЫЙ АНАЛИЗ И ИССЛЕДОВ.ОПЕРАЦИЙ"
                      "\n(14:20-15:55) МАТЕМАТИЧ. МОДЕЛИ ИНФОРМАЦИОН.ПРОЦЕССОВ И УПРАВЛЕНИЯ",

                      "(8:30-10:05) -------------------"
                      "\n(10:25-12:00) Физика (лек.)"
                      "\n (12:30-14:05) Физика (лаб.)",

                      "(8:30-10:05) МАТЕМАТИЧЕСКИЕ МОДЕЛИ ИНФ.ПР. И УПРАВЛЕНИЯ "
                      "\n(10:25-12:00) Математика (лек.)"
                      "\n (12:30-14:05) СИСТЕМНЫЙ АНАЛИЗ (лаб)",

                      "(8:30-10:05) Экономическая теория"
                      "\n(10:25-12:00) ТЕОРИЯ ЭЛЕКТРИЧЕСКИХ ЦЕПЕЙ (лек.)"
                      "\n (12:30-14:05) Физкультура"
                      "\n(14:20-15:55) Психология (пр.)",

                      'ТУПА АДЫХАЕМ',

                      'ТУПА АДЫХАЕМ',
                      ]
timetable_bottom_week = ["(8:30-10:05) Социология (пр.)"
                         "\n(10:25-12:00) Математика(пр.)"
                         "\n (12:30-14:05) Теория электр.цепей (пр.)"
                         "\n(14:20-15:55) Экономическая теория (пр.)",

                         "(8:30-10:05) Математика (лец.)"
                         "\n(10:25-12:00) Физкультура"
                         "\n (12:30-14:05) СИСТЕМНЫЙ АНАЛИЗ И ИССЛЕДОВ.ОПЕРАЦИЙ"
                         "\n(14:20-15:55) МАТЕМАТИЧ. МОДЕЛИ ИНФОРМАЦИОН.ПРОЦЕССОВ И УПРАВЛЕНИЯ",

                         "(8:30-10:05) СИСТЕМНЫЙ АНАЛИЗ (пр.)"
                         "\n(10:25-12:00) Физика (лек.)"
                         "\n (12:30-14:05) Физика (лаб.)"
                         "\n (14:20-15:55) Физика (пр.)",

                         "(8:30-10:05) Социология (лек.)  "
                         "\n(10:25-12:00) Математика (лек.)"
                         "\n (12:30-14:05) Математическо моделирование (лаб.)"
                         "\n (14:20-15:55) Математическо моделирование (лаб.)",

                         "(8:30-10:05) Экономическая теория"
                         "\n(10:25-12:00) ТЕОРИЯ ЭЛЕКТРИЧЕСКИХ ЦЕПЕЙ (лек.)"
                         "\n (12:30-14:05) Физкультура"
                         "\n(14:20-15:55) Математика (пр.)",

                         'ТУПА АДЫХАЕМ',

                         'ТУПА АДЫХАЕМ',

                         ]
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            day_number = datetime.datetime.now().weekday()
            # day_number = datetime.datetime(2020, 9, 22).weekday()
            print(day_number)
            week_number = datetime.date.isocalendar(datetime.datetime.now())[1]
            # week_number = datetime.datetime.isocalendar(datetime.datetime(2020, 9, 27))[1]
            print(week_number)
            if week_number % 2 == 0:
                timetable = timetable_bottom_week
            else:
                timetable = timetable_top_week
            msg_text = week_day_list[day_number] + ":\n" + timetable[day_number]
            if event.user_id == "381750587":
                msg_text = week_day_list[day_number] + "💙💙💙:\n" + timetable[day_number]
            write_msg(event.user_id, msg_text)
