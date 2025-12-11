import requests
import re
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

"""Собираем данные с сайта"""
def func():
    url = 'https://www.banki.ru/news/lenta/'
    page = requests.get(url)

    filteredNews = []
    allNews = []
    soup = BeautifulSoup(page.text, "html.parser")

"""Фильтруем выделенные новости по тематике"""
    allNews =soup.find_all('a', class_='lf473447f text-weight-medium', string=re.compile(r'вклад', re.IGNORECASE)) 

    for data in allNews:
        filteredNews.append(data.text)

    res = [re.sub(r'/\n','', i) for i in filteredNews]
    res = [re.sub(r'\t','', i) for i in filteredNews]
    
    return '  '.join(res)

"""Создаем бота для отправки новостей"""
async def send_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = func()
    await context.bot.send_message(chat_id=CHAT_ID, text=result)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("send", send_result))

    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)
  
if __name__ == '__main__':
    main()
