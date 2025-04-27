from sqlalchemy import select

from database.enumur import UserToAI
from database.models import User, Message
from database.session import async_session


async def get_or_create_user(user_data: dict):
    async with async_session() as session:
        user_id = int(user_data.get("id"))

        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                id=user_id,
                username=user_data.get('username', ''),
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', '')
            )
            session.add(user)
            try:
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
            await session.refresh(user)

        return user


async def save_message(user_id: int, text: str, message_type: UserToAI):
    async with async_session() as session:
        message = Message(
            user_id=user_id,
            text=text,
            message_type=message_type.value
        )
        session.add(message)
        await session.commit()

async def get_dialog_history(user_id: int) -> list[tuple[UserToAI, str]]:
    async with async_session() as session:
        result = await session.execute(
            select(Message)
            .where(Message.user_id == user_id)
            .order_by(Message.created_at)
        )
        messages = result.scalars().all()
        return [(UserToAI(msg.message_type), msg.text) for msg in messages]

async def get_user_history(user_id: int) -> list[tuple[UserToAI, str]]:
    async with async_session() as session:
        result = await session.execute(
            select(Message)
            .where(Message.user_id == user_id)
            .order_by(Message.created_at)
        )
        messages = result.scalars().all()
        return [(UserToAI(msg.message_type), msg.text) for msg in messages]