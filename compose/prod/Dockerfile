# Используем базовый образ с Python
FROM python:3.9-slim

# Устанавливаем рабочий каталог
WORKDIR /app

# Устанавливаем figlet и другие зависимости
RUN apt-get update && apt-get install -y \
    figlet \
    build-essential \
    python3-dev \
    libmariadb-dev \
    libmariadb-dev-compat \
    netcat-openbsd \
    gettext-base \
    && apt-get clean

# Копируем requirements.txt и устанавливаем зависимости
COPY backend/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

# Копируем необходимые файлы в контейнер
COPY backend /app/

# Указываем команду для запуска
CMD ["sh", "start.sh"]
