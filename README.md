# REST API Backend приложение

### Задание 
>Реализовать REST backend с использование DRF (Django Rest Framework) новостного приложения   

1. Сохранение в БД Новостей и их Типов
2. Новость должна иметь структуру:
- Имя
- Краткое описание
- Полное описание
- Тип новости
3. Тип новостей должен иметь структуру:
- Имя
- Цвет

### Функционал
- CRUD (Create, Read, Update, Delete) типов новостей    
- CRUD новостей 
- Возможность получить список всех типов новостей   
- Возможность получить список всех новостей (имя, краткое описание, имя типа, цвет типа)    
- Возможность получить список новостей определенного типа   

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/p2cbbb/news_api
cd news_api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Устанавливаем переменные окружения
В папке `config` создать файл `.env` и заполнить eго ключами

```bash
SECRET_KEY=<secret_key>
DEBUG=<debug>
```

### Применение миграций, создания суперпользователя и запуск проекта
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```