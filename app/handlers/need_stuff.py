"""
Скрипт поиска дополнительно сотрудника
"""

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from app.message_states import MessageState, CHANNEL_NAME


async def message_help1(message: types.Message):
    await message.answer("Когда вам нужен дополнительный сотрудник?\n\nПример: 20 июля")
    await MessageState.message4.set()


async def message_help2(message: types.Message, state: FSMContext):
    await state.update_data(group1=message.text)
    await message.answer(
        "Напишите адрес и номер ПВЗ, на который нужен доп.сотрудник?\n\nПример: Улица Профсоюзная 1, КЗН-1"
    )
    await MessageState.message5.set()


async def message_help3(message: types.Message, state: FSMContext):
    await state.update_data(group2=message.text)
    await message.answer(
        "Со скольки до скольки вам нужен доп.сотрудник?\n\nПример: 15:00-18:00 или 15-18"
    )
    await MessageState.message6.set()


async def send_help(message: types.Message, state: FSMContext):
    await state.update_data(group3=message.text)
    change_data = await state.get_data()
    await message.bot.send_message(
        CHANNEL_NAME,
        f"Требуется дополнительный сотрудник на дату: <b>{change_data['group1']}</b>,\n\n"
        f"Адрес и номер ПВЗ: <b>{change_data['group2']}</b>.\n\n"
        f"Время на которое требуется дополнительный сотрудник: <b>{change_data['group3']}</b>,\n\n"
        f"Ник администратора в телеграмме - {'@'+message.from_user.username}",
        parse_mode=types.ParseMode.HTML,
    )
    await state.finish()
    await message.answer("Ваше сообщение отправлено в группу поиска, ждите ответа.")


def register_handlers_stuff(dp: Dispatcher):
    dp.register_message_handler(message_help1, commands="stuff", state="*")
    dp.register_message_handler(
        message_help1, Text(equals="Нужен доп.сотрудник", ignore_case=True), state="*"
    )
    dp.register_message_handler(message_help2, state=MessageState.message4)
    dp.register_message_handler(message_help3, state=MessageState.message5)
    dp.register_message_handler(send_help, state=MessageState.message6)
