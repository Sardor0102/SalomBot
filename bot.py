import logging
from aiogram import Bot, Dispatcher, executor, types


bot_token = "6972562005:AAETXUjDtm0tG8piNmM195rdwYyiZF8rjoA"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token, parse_mode='html')

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command_bot(message: types.Message):
    await message.answer(f"Salom, @<b>{message.from_user.username}!</b>")




async def command_menu(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Ishga tushirish'),
        ]
    )


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=command_menu)
