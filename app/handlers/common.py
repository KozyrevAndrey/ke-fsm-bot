
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


text_help1 = "Ботом, можно управлять командами /start, /help, /cancel, /stuff и /change.\n" \
             "/start - Данная команда выводит информацию, которая появляется при первом нашем знакомстве.\n" \
             "/help - Помогает вам разобраться в командах и работе бота.\n" \
             "/cancel - Отменяет введенные сообщения, не работает на отправленном сообщении." \
             " Может отменить первые два введенных сообщения.\n" \
             "/stuff - Команда создана для поиска дополнительного сотрудника, также работает с кнопкой 'Найти доп.сотрудника'." \
             "Вам нужно будет ответить на три вопроса и ответы будет отправлены в понятном виде в группу поиска.\n" \
             "/change - команда аналогичная поиску доп.сотрудника, только она создана для поиска замены.\n" \
             "По вопросам и предложения пишите @AigulBabay"


async def hello_there(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Нужен доп.сотрудник', 'Нужна замена']
    keyboard.add(*buttons)
    await message.answer(f'Привет, {message.from_user.full_name}, я - Бот Василий\n'
                         f'Мое предназначение - помочь Вам найти замену или дополнительного сотрудника на помощь.\n'
                         f'Чтобы приступить к поиску нажмите на нужную Вам кпонку или введите команду, '
                         f'также можете приступить к поиску через меню: "Найти доп.сотрудника" или /stuff, и "Найти замену" или /change\n'
                         f'Мной Вы можете управлять через команды /start, /help, /cancel и также через кнопки, созданные для поиска',
                         reply_markup=keyboard)


async def help_me(message: types.Message):
    await message.answer(text_help1)


async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Отменять нечего, можете спокойно писать.")
    else:
        await state.finish()
        await message.reply("Действие отменено,\n"
                            "Введите /start и начните заново")


def register_handlers_common(dp: Dispatcher, admin_id: int):
    dp.register_message_handler(hello_there, commands="start", state="*")
    dp.register_message_handler(help_me, commands="help", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")

