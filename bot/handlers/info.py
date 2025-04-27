from aiogram import Router, F
from aiogram.types import Message
from database.crud import get_or_create_user

router = Router()


@router.message(F.text == "ℹ️ Инфо")
async def info_handler(message: Message):
    try:
        user = await get_or_create_user({
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name
        })

        if not user.created_at:
            return await message.answer("Сначала выполните команду /start")

        info_text = (
            f"ID: {user.id}\n"
            f"Username: @{user.username}\n"
            f"Имя: {user.first_name}\n"
            f"Фамилия: {user.last_name}\n"
            f"Дата регистрации: {user.created_at.strftime('%d.%m.%Y %H:%M')}"
        )

        await message.answer(info_text)

    except Exception as e:
        await message.answer("Произошла ошибка, попробуйте позже")
        print(f"Error in info handler: {str(e)}")