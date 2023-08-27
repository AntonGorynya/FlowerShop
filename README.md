# FlowerShop

Магазин цветов

## Установка test

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
Выполните миграцию

```python
FlowerShop> python .\manage.py migrate  
```