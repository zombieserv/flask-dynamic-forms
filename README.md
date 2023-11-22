# Flask Dynamic Forms

Это простое Flask-приложение, которое позволяет создавать и хранить динамические формы.

## Запуск приложения

1. Убедитесь, что у вас установлен Docker и Docker Compose.

2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/zombieserv/flask-dynamic-forms
   cd flask-dynamic-forms
   
3. Скопируйте файл .env и установите значения переменных окружения:
    ```bash
   cp .env.sample .env

4. Запустите Docker Compose
     ```bash
       docker-compose up --build

5. Приложение будет доступно по адресу http://localhost:5000

## Структура проекта
`main.py` - Основной файл приложения, содержащий точку входа и роутинг

`models.py` - Модели данных для работы с MongoDB.

`middleware.py` - Промежуточные обработчики Flask (для валидации данных).

`populate.py` - Скрипт для наполнения базы данных начальными данными.

`tests.py` - Тесты для проверки функциональности API.

`utils.py` - Вспомогательные утилиты (включая функцию поиска соответствующей формы).

`validate.py` - Модуль для валидации данных форм.

## Импорт конфига тестов в Insomnia
Для ручного тестирования прилагается профиль в [Insomnia](https://insomnia.rest/), следуйте [этой инструкции](https://docs.insomnia.rest/insomnia/import-export-data).
Используйте следующую ссылку для импорта: [Insomnia_2023-11-22.json](https://raw.githubusercontent.com/zombieserv/flask-dynamic-forms/master/)