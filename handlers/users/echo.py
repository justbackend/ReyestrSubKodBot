from aiogram import types
from loader import dp


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)
