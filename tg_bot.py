from parser import AvitoParse
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, TG_USER_ID, UPDATE_TIME, SETTINGS
import json
from aiogram.utils.markdown import hbold, hcode, hlink
from aiogram.dispatcher.filters import Text

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все посты", "Последние пять постов", "Свежие посты"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("AvitoBot", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все посты"))
async def get_all_posts(message: types.Message):
    with open("items.json", encoding="utf-8") as file:
        post_list = json.load(file)
    for k, v in sorted(post_list.items()):
        post = f"{hlink(v['name'], v['url'])}\n\n{hcode(v['description'])}\n\n{hbold(v['price'] + ' rub.')}"
        await message.answer(post)


@dp.message_handler(Text(equals="Последние пять постов"))
async def get_last_five_posts(message: types.Message):
    with open("items.json", encoding="utf-8") as file:
        post_list = json.load(file)
    for k, v in sorted(post_list.items())[-5:]:
        post = f"{hlink(v['name'], v['url'])}\n\n{hcode(v['description'])}\n\n{hbold(v['price'] + ' rub.')}"
        await message.answer(post)


@dp.message_handler(Text(equals="Свежие посты"))
async def get_fresh_posts(message: types.Message):
    fresh_posts = AvitoParse(**SETTINGS).check_update()
    if len(fresh_posts) >= 1:
        for k, v in sorted(fresh_posts.items()):
            post = f"{hlink(v['name'], v['url'])}\n\n{hcode(v['description'])}\n\n{hbold(v['price'] + ' rub.')}"
            await message.answer(post)
    else:
        await message.answer("Пока нет новых предложений...")


async def posts_every_time():
    while True:
        fresh_posts = AvitoParse(**SETTINGS).check_update()
        if len(fresh_posts) >= 1:
            for k, v in sorted(fresh_posts.items()):
                post = f"{hlink(v['name'], v['url'])}\n\n{hcode(v['description'])}\n\n{hbold(v['price'] + ' rub.')}"
                await bot.send_message(TG_USER_ID, post)
        await asyncio.sleep(UPDATE_TIME)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(posts_every_time())
    executor.start_polling(dp)
