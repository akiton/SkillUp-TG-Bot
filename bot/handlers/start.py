from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database.crud import get_or_create_user
from bot.keyboards import main_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    _ = await get_or_create_user({
        'id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name
    })

    await message.answer(
        f"Привет! Я AI бот {"Пюрешка"}. Отправь мне любой математический пример, который я смогу решить для тебя!",
        reply_markup=main_keyboard()
    )