# FlowerShop

Магазин цветов

## Установка

```commandline
python -m pip install -r requirements.txt
```
Перед запуском создайте файл .env вида:
```commandline
TELEGRAM_KEY='хххх:уууу'
CHAT_ID='ID вашего чата'
ACCOUNT_ID='ID вашего магазина'
U_KEY='Ключ к юкассе'
```
- Токен для Телеграм бота вы можете получить https://telegram.me/BotFather
- Для получения CHAT_ID напишите любое сообщение вашему боту, после чего перейдите по ссылке https://api.telegram.org/bot{TG_TOKEN}/getUpdates

## Запуск
Вы можете создать ключ выполнив команду
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

```
Создайте файл базы данных SQLite и отмигрируйте её следующей командой:

```python
python .\manage.py migrate  
```
Создайте супер пользователя
```python
python manage.py createsuperuser
```
Соберите статику
```python
python manage.py collectstatic
```

Запустите сервер:
```
python manage.py runserver
```

Откройте сайт в браузере по адресу http://127.0.0.1:8000/.