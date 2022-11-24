import time
import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN
from model import RecipeModel, preparation

RecipeModel = RecipeModel()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

b1 = KeyboardButton('/Рецепт')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b1)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!", reply_markup=kb)


@dp.message_handler(commands=['Рецепт'])
async def start_handler(message: types.Message):
    letters = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    prompt = '<s>' + ''.join(random.choice(letters) for i in range(random.randint(2, 6))) + 'Название: '
    await message.answer(preparation(RecipeModel.generate_text(prompt)))

if __name__ == '__main__':
    executor.start_polling(dp)
