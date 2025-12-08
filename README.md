# Web-scraping-telegram-bot
Web scraping telegram bot
## Возможности кода
Представленный код позволяет реализовать поиск новостей на популярном сайте banking.ru, выделение наиболее интересных новостей и только в интересующей тематике (в представленной версии - в отношении новостей о вкладах) и их публикацию в telegram боте по запросу пользователя. 

### Как запустить?

Копируем репозиторий:
git clone https://github.com/Yuriy-Grishin/tgbotwebscraping.git
Cоздаем виртуальное окружение:
python -m venv env
source venv/bin/activate
Устанавливаем зависимость с requirements.txt:
pip install -r requirements.txt

Создаем файл .env со следующим содержанием:
BOT_TOKEN = 'указываем токен бота'
CHAT_ID = 'указываем id вашего чата'
Создаем образ: docker build -t yuriygrishin/foodgram-backend:latest .
Перейти в папку infra: cd infra и запускаем команду docker-compose up
Сделай миграции, статику, суперпользователя:
docker-compose exec -T backend python manage.py makemigrations
docker-compose exec -T backend python manage.py migrate
docker-compose exec -T backend python manage.py collectstatic --no-input
docker-compose exec web python manage.py createsuperuser
Введи в браузере: 51.250.67.176/signup

## В работе использовались:
Python
Django
DRF
Docker
Postgres
Nginx
cd 
