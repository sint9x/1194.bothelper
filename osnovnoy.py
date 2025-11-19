import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router


#logging.basicConfig(level = logging.info)
#logger = logging.getLogger(__name__)

BOT_TOKEN = "8269579411:AAFIV5AT5Wkt8t_aX8LFwh2sUDG034ikMss"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

first_aid_instructions = {
    "перелом": """Оказание помощи при переломе:""",
    "ожог": """Оказание помощи при ожоге:"""


}
def get_main_keyboard():
    buttons = [
        KeyboardButton(text='Перелом'),
        KeyboardButton(text='Ожог'),
        KeyboardButton(text='Кровотечение'),
        KeyboardButton(text='Удушье'),
        KeyboardButton(text='Отравление'),
        KeyboardButton(text='Обморок'),
        KeyboardButton(text='ℹ️ О боте')
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[buttons[i:i+2] for i in range(0, len(buttons), 2)],
        resize_keyboard=True
    )
    return keyboard

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = """
🚑 <b>Бот первой помощи</b>

Я предоставляю инструкции по оказанию первой помощи при различных травмах и неотложных состояниях.

Выберите тип травмы из меню ниже.

<b>ВАЖНО:</b> При серьезных травмах обязательно вызывайте скорую помощь!
    """
    await message.answer(welcome_text, parse_mode='HTML', reply_markup=get_main_keyboard())


@router.message()
async def handle_buttons(message: types.Message):
    text = message.text

    if text == 'Перелом':
        await message.answer(first_aid_instructions["перелом"])
    elif text == 'Ожог':
        await message.answer(first_aid_instructions["ожог"])

async def main():
    #logger.info("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
        #logger.info("Бот остановлен")