from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyborad_2
from keboard.key_inline import get_keyboard_inline

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)




async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот ')

    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message:types.Message):
    await message.answer('Привет, я твой первый ЭХО бот ', reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.hibiny.ru/images/board/1038092/big/8e39774efbbb353d4cb83504efb539cc.jpg', caption='Вот тебе кот!!', reply_markup=get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyborad_2())




@dp.message_handler(lambda message:message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://s00.yaplakal.com/pics/pics_original/7/6/4/6613467.jpg', caption='Вот тебе собака!!')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_1())



@dp.message_handler(commands= 'help')
async def help(message:types.Message):
    await message.reply('Я могу помочь тебе c ....')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher. bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
