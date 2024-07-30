from aiogram import types
from loader import bot

async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='Botni ishga tushurish'),
            types.BotCommand(command="help", description="Yordam"),
            types.BotCommand(command="finish", description="Excel formatida yuklab olish"),
            types.BotCommand(command="admin", description="Faqat adminlar uchun"),
        ]
    )