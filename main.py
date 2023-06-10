from aiogram import Bot, Dispatcher, executor, types

f = open("C:/Users/filos/Desktop/token_api.txt", 'r')
TOKEN_API = f.read()
f.close()

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(text='Добро пожаловать в нашего бота!')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)