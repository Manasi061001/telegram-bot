import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from example import example

bot = Bot(token='YOUR-TOKEN')
dp = Dispatcher(bot)

openai.api_key = os.environ['OPENAI_API_KEY']

example()
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
 await message.reply('Hello! I am GPT Chat BOT. You can ask me anything :)')
@dp.message_handler()
async def gpt(message: types.Message):
 response = openai.Completion.create(model="text-davinci-003",
                   prompt=message.text,
                   temperature=0.5,
                   max_tokens=1024,
                   top_p=1,
                   frequency_penalty=0.0,
                   presence_penalty=0.0)
 await message.reply(response.choices[0].text)

if _name_ == "_main_":
 executor.start_polling(dp)
