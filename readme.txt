Запуск проекта на Linux/ubuntu

- 'pyton3 -m venv venv' - создайте виртуальное окружение
- 'source venv/bin/activate' - войдите в виртуальное окружение
- 'pip install -r requirements.txt' - установка зависимостей
- установите базу данный postgresql
    - # создайте фаил конфигурации репозитория:
    sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

    # Импортируйте ключ подписи репозитория:
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    
    #Обновите списки пакетов:
    sudo apt-get update

    # Установка последней версии PostgreSQL.
    sudo apt-get -y install postgresql
- 'pip install psycopg2' -  установка модуля для PostgreSQL


