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

### Команда для запуска проекта через docker
```bash
docker-compose up --build
```

### Эндпоинты
#### Новости
- `GET /api/news-items/` - получить список всех новостей. Чтобы добавить фильтрацию по определенному типу новостей добавить `?news_type=<news_type>`
- `GET /api/news-items/<id>/` - получить статью с указанным id
- `POST /api/news-items/` - создать новую статью
- `PUT /api/news-items/<id>/` - изменяет статью с указанным id
- `DELETE /api/news-items/<id>/` - удаляет статью с указанным id

##### Получение и отправка данных произодится в формате JSON:
```json
[
    {
        "title": "Название статьи",
        "about": "Краткое описание статьи",
        "description": "Полное описание статьи",
        "news_type_name": "Тип статьи",
        "news_type_color": "Цвет типа"
    },
]
```
##### Ответ при создании новой статьи:
```json
{
    "status": "news item has been created"
}
```
##### Ответ при удалении статьи:
```json
{
    "status": "news item has been deleted"
}
```

#### Тип новостей
- `GET /api/news-types/` - получить список всех типов новостей
- `GET /api/news-types/<id>/` - получить тип новости с указанным id
- `POST /api/news-types/` - создать новый тип новости
- `PUT /api/news-types/<id>/` - изменить тип новости с указанным id
- `DELETE /api/news-types/<id>/` - удалить тип новости с указанным id

##### Получение и отправка данных произодится в формате JSON:
```json
[
    {
        "name": "Спорт",
        "color": "RED"
    },
    {
        "name": "Политика",
        "color": "BLUE"
    },
]
```

##### Ответ при создании нового типа новости:
```json
{
    "status": "news type has been created"
}
```
##### Ответ при удалении типа новости:
```json
{
    "status": "news type has been deleted"
}
```