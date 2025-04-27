from aiogram import Router, F
from aiogram.types import Message

from ai.ai_handler import AIHandler
from database.crud import get_user_history, save_message
from database.enumur import UserToAI

router = Router()
ai_handler = AIHandler()


@router.message(F.text)
async def echo_handler(message: Message):
    user_id = message.from_user.id
    user_message = message.text

    history = await get_user_history(user_id)

    await save_message(user_id, user_message, UserToAI.user)

    ai_response = await ai_handler.generate_response(history)

    await save_message(user_id, ai_response, UserToAI.ai)

    await message.answer(ai_response)