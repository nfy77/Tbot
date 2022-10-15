from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3

available_gender = ["Господин", "Госпожа"]
connect = None
cursor = None

class RegistrationForm(StatesGroup):
    waiting_for_gender = State()
    waiting_for_name = State()
    waiting_for_birthday = State()
# TODO координаты    

async def registration_start(message: types.Message):
    # запишем номер пользователя
    user = [message.from_user.id, '', '', '']
    #check if exist
    cursor.execute(f"SELECT * FROM users WHERE id = {user[0]}")
    row = cursor.fetchone()    
    if row is None:
        #add bd
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
        connect.commit() 
    else:
        await message.answer("А я тебя уже знаю! Ты "+str(row[1])+" "+str(row[2])+", родился "+str(row[3]))
        await message.answer("Если не хочешь менять данные, жми /cancel")                

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_gender:
        keyboard.add(size)

    await message.answer("Как к вам обращаться?", reply_markup=keyboard)
    await RegistrationForm.waiting_for_gender.set()

async def gender_entered(message: types.Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    
    if message.text not in available_gender:
        await message.answer("Пожалуйста, выберите обращение, используя клавиатуру ниже.")
        return
    await state.update_data(gender=message.text)
    # для простых шагов можно не указывать название состояния, обходясь next()
    await RegistrationForm.next()
    await message.answer("Введите свое имя:",  reply_markup=types.ReplyKeyboardRemove())
    
async def name_entered(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    # для простых шагов можно не указывать название состояния, обходясь next()
    await RegistrationForm.next()
    await message.answer("Отличное имя, запомню! А теперь введите свой день рождения:", reply_markup=types.ReplyKeyboardRemove())
    
async def birthday_entered(message: types.Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    user_data = await state.get_data()
    await message.answer(f"Вас величают {user_data['gender']} {user_data['name']}, вы родились {user_data['birthday']}.\n"           
                         f"Попробуйте теперь узнать гороскоп: /horodru или пройти тест на депрессию /beckscale. Можем повторить /registration", reply_markup=types.ReplyKeyboardRemove())
    
    # запишем всю инфу в бд
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (user_data['name'], user_data['id'],))
    connect.commit() 
    cursor.execute("UPDATE users SET gender = ? WHERE id = ?", (user_data['gender'], user_data['id'],))
    connect.commit() 
    cursor.execute("UPDATE users SET birthday = ? WHERE id = ?", (user_data['birthday'], user_data['id'],))
    connect.commit()     
    await state.finish()

def register_handlers_registration(dp: Dispatcher, con: sqlite3.connect, cur: sqlite3.Cursor):
    dp.register_message_handler(registration_start, commands="registration", state="*")
    dp.register_message_handler(gender_entered,     state=RegistrationForm.waiting_for_gender)
    dp.register_message_handler(name_entered,       state=RegistrationForm.waiting_for_name)    
    dp.register_message_handler(birthday_entered,   state=RegistrationForm.waiting_for_birthday)
    # связь с бд
    global connect
    global cursor
    connect = con
    cursor = cur
