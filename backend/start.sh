#!/bin/sh

# figlet
echo "Starting Django..."
figlet -c "BACKEND"

# Выполнение миграций
echo "Running migrations..."
python manage.py migrate

# Запуск сервера
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
