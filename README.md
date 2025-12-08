# Web-scraping-telegram-bot
Web scraping telegram bot
## Возможности кода
Представленный код позволяет реализовать поиск новостей на популярном сайте banking.ru, выделение наиболее интересных новостей и только в интересующей тематике (в представленной версии - в отношении новостей о вкладах) и их публикацию в telegram боте по запросу пользователя. 

### Как запустить?

Копируем репозиторий:
git clone https://github.com/Yuriy-Grishin/Web-scraping-telegram-bot.git
Cоздаем виртуальное окружение:
python -m venv env
source venv/bin/activate
Устанавливаем зависимость с requirements.txt:
pip install -r requirements.txt

Создаем файл .env со следующим содержанием:
BOT_TOKEN = 'указываем токен бота'
CHAT_ID = 'указываем id вашего чата'

## В работе использовались:
Python
Beautiful Soup 4(bs4) 
Requests
Python-telegram-bot


