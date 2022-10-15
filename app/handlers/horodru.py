from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3

import re
import datetime

def check_date_format(date):
    for not_num in re.findall(r'[^0-9]+', date):
        date = date.replace(not_num, '.')
    try:
      date = datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
      print('Invalid date!')
    return date

connect = None
cursor = None

horo_id = 1000

class HorodruForm(StatesGroup):
    waiting_for_data = State()

async def horodru_start(message: types.Message):
    # инфо о гороскопе друидов
    cursor.execute(f"""SELECT horo_head.type, horo_text.text 
                         FROM horo_head 
                         INNER JOIN horo_text ON horo_head.text_id = horo_text.text_id          
                         WHERE horo_id = {horo_id}""")
    row = cursor.fetchone()
    await message.answer(f"{row[1]}", reply_markup=types.ReplyKeyboardRemove())

    #check if exist
    cursor.execute(f"SELECT * FROM users WHERE id = {message.from_user.id}")
    row = cursor.fetchone()    
    if row is None:
        await message.answer("Введите дату:", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Использовать твою дату рождения?")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(row[3])

        await message.answer("Можешь ввести другую дату:", reply_markup=keyboard)

    await HorodruForm.waiting_for_data.set()

async def data_entered(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    user_data = await state.get_data()
#    await message.answer(f"Вы ввели дату {user_data['date']}", reply_markup=types.ReplyKeyboardRemove())
    # приводим дату к формату
    # TODO ввод даты без разделителей
    date = check_date_format(user_data['date'])
    date = date.replace(year=1900) # гороскоп друидов храниться 1900 годом
    date = date.strftime("%Y%m%d")

    cursor.execute(f"""SELECT horo_sign.sign, horo_text.text 
                         FROM horo_head 
                         INNER JOIN horo_sign ON horo_head.horo_id = horo_sign.horo_id
                         INNER JOIN horo_text ON horo_sign.text_id = horo_text.text_id                         
                         WHERE horo_head.horo_id = {horo_id}
                         AND {date} BETWEEN date_begin AND date_end""")

    row = cursor.fetchone()
    print(message.from_user.id, row[0])
    await message.answer(f"Вы - {row[0]}!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"{row[1]}", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

def register_handlers_horodru(dp: Dispatcher, con: sqlite3.connect, cur: sqlite3.Cursor):
    dp.register_message_handler(horodru_start, commands="horodru", state="*")
    dp.register_message_handler(data_entered,  state=HorodruForm.waiting_for_data)
    # связь с бд
    global connect
    global cursor
    connect = con
    cursor = cur
