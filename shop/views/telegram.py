
from aiogram import Bot

TOKEN = '8428931730:AAE862ooa4fChNKUh_MGjdiTrgueGdcoUNo'
ADMINS = '6639088087'

async def send_message(text):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=ADMINS, text = text, parse_mode='HTML')
    bot.close()

