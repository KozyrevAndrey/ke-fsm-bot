from aiogram.dispatcher.filters.state import State, StatesGroup

from app.config_reader import load_config

config = load_config("config/bot.ini")

# -1001670699026
CHANNEL_ID = config.tg_bot.group_id


class MessageState(StatesGroup):
    message1 = State()
    message2 = State()
    message3 = State()
    message4 = State()
    message5 = State()
    message6 = State()
