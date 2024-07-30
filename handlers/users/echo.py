import io

from aiofiles import os
from aiogram import types
from aiogram.filters import Command
from aiogram.types import BufferedInputFile

from loader import dp
import pandas as pd

collected_data = []


def parse_data(text):
    data = {}
    lines = text.strip().split('\n')
    for line in lines:
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            data[key] = value
        else:
            pass
    return data


def create_excel(data):
    df = pd.DataFrame(data)
    output_file = 'shipment_data.xlsx'
    df.to_excel(output_file, index=False)
    return output_file


@dp.message(lambda message: not message.text.startswith('/'))
async def handle_text(message: types.Message):
    data = parse_data(message.text)
    collected_data.append(data)


@dp.message(Command(commands='finish'))
async def handle_stop(message: types.Message):
    try:
        if not collected_data:
            await message.reply("No data to export.")
            return

        excel_file = create_excel(collected_data)

        with open(excel_file, 'rb') as file:
            file_bytes = file.read()

        file_object = BufferedInputFile(file_bytes, filename='shipment_data.xlsx')

        await message.reply_document(file_object)

        await os.remove(excel_file)
        collected_data.clear()

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
