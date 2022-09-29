from aiogram import Bot, Dispatcher, types, executor
from handlers import *

API_Token = '5626308217:AAEO-q8ppul8rXTqR23JonI1hXxXigkQrrM'

bot = Bot(token=API_Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text='Hello!', reply_markup=keyboard_markup)


if __name__ == '__main__':
    executor.start_polling(dp)
