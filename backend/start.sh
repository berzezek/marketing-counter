#!/bin/sh

echo "Waiting for MySQL..."
while ! nc -z mysql-db 3306; do
  echo "Waiting for MySQL to be available...sleeping for 20s..."
  sleep 20
done

# figlet
echo "Starting Django..."
if command -v figlet > /dev/null 2>&1; then
    figlet -c "BACKEND"
else
    echo "figlet is not installed."
fi

# Выполнение миграций
echo "Running migrations..."
if ! python manage.py migrate; then
    echo "Migrations failed!"
    exit 1
fi

# collectstatic
echo "Collecting static files..."
if ! python manage.py collectstatic --noinput; then
    echo "Collecting static files failed!"
    exit 1
fi

# Запуск сервера
echo "Starting server..."
exec gunicorn --bind 0.0.0.0:8000 core.wsgi:application
