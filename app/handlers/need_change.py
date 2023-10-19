"""
Скрипт для поиска замены
"""

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from app.message_states import MessageState, CHANNEL_ID


async def message1_stuff(message: types.Message):
    await message.answer("Когда Вам нужна замена?\n\nПример: 20 июля")
    await MessageState.message1.set()


async def message2_stuff(message: types.Message, state: FSMContext):
    await state.update_data(message_group1=message.text)
    await message.answer(
        "Напишите адрес и номер ПВЗ, на который нужна замена?\n\nПример: Улица Профсоюзная 1, КЗН-1"
    )
    await MessageState.message2.set()


async def message3_stuff(message: types.Message, state: FSMContext):
    await state.update_data(message_group2=message.text)
    await message.answer(
        "Со сколько до скольки вам нужна замена?\n\nПример: 15:00-18:00 или 15-18"
    )
    await MessageState.message3.set()


async def send_info(message: types.Message, state: FSMContext):
    await state.update_data(message_group3=message.text)
    data = await state.get_data()
    await message.bot.send_message( 
        CHANNEL_ID,
        f"Требуется замена на дату: <b>{data['message_group1']}</b>,\n\n"
        f"Адрес и номер ПВЗ: <b>{data['message_group2']}</b>,\n\n"
        f"Время на которое требуется замена: <b>{data['message_group3']}</b>,\n\n"
        f"Ник администратора в телеграмме - {'@'+message.from_user.username}",
        parse_mode=types.ParseMode.HTML,
    )
    await state.finish()
    await message.answer("Ваше сообщение отправлено в группу поиска, ждите ответа.")


def register_handlers_change(dp: Dispatcher):
    dp.register_message_handler(message1_stuff, commands="change", state="*")
    dp.register_message_handler(
        message1_stuff, Text(equals="Нужна замена", ignore_case=True), state="*"
    )
    dp.register_message_handler(message2_stuff, state=MessageState.message1)
    dp.register_message_handler(message3_stuff, state=MessageState.message2)
    dp.register_message_handler(send_info, state=MessageState.message3)
