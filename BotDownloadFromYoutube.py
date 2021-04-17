import pytube
from pytube import YouTube
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import telebot
import time


bot = telebot.TeleBot(token="1671450952:AAHsVNOu_Fp6LrPvwAQYwxGZ-sDFzgMMxH8")


@bot.message_handler(commands=['start', 'help',])
def first_or_help_commands(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне ссылку на видео, я скачаю тебе его.:) ")


@bot.message_handler(content_types=['text'])
def download_video(message):
    youtube = pytube.YouTube(message.text)
    video = youtube.streams.first()
    video.download('../Video')
    bot.send_message(message.chat.id, "Подожди мгновение я колдую..Вжух")
    time.sleep(1)
    video_location = video.title
    video_adr = open(f'../Video/{video_location}.mp4', 'rb')
    bot.send_video(message.chat.id, video_adr)

    bot.send_message(message.chat.id, "А вот и твое видео")
    bot.send_message(message.chat.id, "Отправь мне еще ссылку я тебе что нибудь наколдую...Вжух")

bot.polling()

