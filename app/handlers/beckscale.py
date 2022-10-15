from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3

connect = None
cursor = None

test_id = 1000
available_score = ["1", "2", "3", "4"]
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#for s in available_score:
#    keyboard.add(s)

keyboard.row("1", "2", "3", "4")

class BeckscaleForm(StatesGroup):
    waiting_for_answ = State()

async def beckscale_start(message: types.Message, state: FSMContext):
    # инфо о тесте
    cursor.execute(f"""SELECT test_head.type, test_text.text 
                         FROM test_head 
                         INNER JOIN test_text ON test_head.text_id = test_text.text_id          
                         WHERE test_id = {test_id}""")
    row = cursor.fetchone()
    await message.answer(f"{row[1]}", reply_markup=types.ReplyKeyboardRemove())

    await message.answer("Начнем!", reply_markup=types.ReplyKeyboardRemove())

    async with state.proxy() as data:
        data['answs'] = []
        data['score'] = 0
        data['cur_ques'] = 1

        cursor.execute(f"""SELECT test_ques.ques_id, test_text.text 
                             FROM test_ques 
                             INNER JOIN test_text ON test_ques.text_id = test_text.text_id                         
                             WHERE test_ques.test_id = {test_id}""")
        data['row_ques'] = cursor.fetchall()

        await message.answer(f"Вопрос 1: {data['row_ques'][0][1]}", reply_markup=keyboard)
        cursor.execute(f"""SELECT test_answ.answ_id, test_text.text, test_answ.score 
                            FROM test_answ 
                            INNER JOIN test_text ON test_answ.text_id = test_text.text_id                         
                            WHERE test_answ.test_id = {test_id}
                            AND test_answ.ques_id = {data['row_ques'][0][0]}""")
        row_answ = cursor.fetchall()
        j = 0
        for answ in row_answ:
            j = j + 1
            await message.answer(f"{j}: {answ[1]}", reply_markup=keyboard)

        await BeckscaleForm.waiting_for_answ.set()

async def answ_entered(message: types.Message, state: FSMContext):
    # добавляем ответ в массив
    async with state.proxy() as data:
        if message.text not in available_score:
            await message.answer("Пожалуйста, выберете номер утверждения, который подходит вам больше всего")
            return
        print(message.from_user.id, data['row_ques'][data['cur_ques']][1], int(message.text) - 1)
        data['answs'].append(int(message.text) - 1)
        data['score'] = data['score'] + int(message.text) - 1
        # выводим некст вопрос
        await message.answer(f"Вопрос {data['cur_ques'] + 1}: {data['row_ques'][data['cur_ques']][1]}", reply_markup=keyboard)
        cursor.execute(f"""SELECT test_answ.answ_id, test_text.text, test_answ.score 
                            FROM test_answ 
                            INNER JOIN test_text ON test_answ.text_id = test_text.text_id                         
                            WHERE test_answ.test_id = {test_id}
                            AND test_answ.ques_id = {data['row_ques'][data['cur_ques']][0]}""")
        row_answ = cursor.fetchall()
        j = 0
        for answ in row_answ:
            j = j + 1
            await message.answer(f"{j}: {answ[1]}", reply_markup=keyboard)
        # делаем сразу некст вопрос
        data['cur_ques'] += 1
        # если вопросы кончились то никакого text ни kb не будет делаем проверку
        if data['cur_ques'] == len(data['row_ques']):
            # конец
            print(message.from_user.id, data['score'])
            await message.answer("Поздравляю, тест завершен!", reply_markup=types.ReplyKeyboardRemove())
            if (data['score'] < 14):
                await message.answer("У вас: Нормальное состояние!", reply_markup=types.ReplyKeyboardRemove())
            elif (data['score'] < 20):
                await message.answer("У вас: Легкое депрессивное расстройство", reply_markup=types.ReplyKeyboardRemove())
            elif (data['score'] < 29):
                await message.answer("У вас: Депрессивное расстройство средней степени тяжести",
                                     reply_markup=types.ReplyKeyboardRemove())
            else:
                await message.answer("У вас: Депрессивное расстройство тяжелой степени тяжести",
                                     reply_markup=types.ReplyKeyboardRemove())
            await state.finish()

def register_handlers_beckscale(dp: Dispatcher, con: sqlite3.connect, cur: sqlite3.Cursor):
    dp.register_message_handler(beckscale_start, commands="beckscale", state="*")
    dp.register_message_handler(answ_entered,  state=BeckscaleForm.waiting_for_answ)
    # связь с бд
    global connect
    global cursor
    connect = con
    cursor = cur
