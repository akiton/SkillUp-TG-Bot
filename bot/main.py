import asyncio
import os

from aiogram import Bot, Dispatcher




async def main():


    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    from bot.handlers import info, echo, start

    dp.include_router(info.router)
    dp.include_router(start.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())