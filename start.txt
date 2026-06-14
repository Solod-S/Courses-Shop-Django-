# Начало работы с проектом Courses-Shop-Django

## Установка и настройка окружения через Pipenv

```bash
# Установка Pipenv
python -m pip install pipenv

# Установка Django 4.0.8
python -m pipenv install django==4.0.8

# Активация виртуального окружения Pipenv
python -m pipenv shell

# Получить полный путь к виртуальному окружению
python -m pipenv --venv
```

Пример пути к виртуальному окружению:

```text
C:\Users\Sergey\Documents\test\Courses-Shop-Django-\.venv\Scripts\python.exe
```

```bash
# Выход из виртуального окружения
exit
```

## Проверка установки

```bash
# Проверка версии Django
python -m django --version

# Список установленных пакетов
pip list

# Граф зависимостей пакетов
pip graph
```

## Создание проекта Django

```bash
# Создание проекта Django в текущей папке
django-admin startproject base .
```

## Запуск на macOS

```bash
# Создание виртуального окружения
python3 -m venv .venv

# Активация виртуального окружения
source .venv/bin/activate

# Обновление pip
python -m pip install --upgrade pip

# Установка Django 4.0.8
python -m pip install Django==4.0.8

# Применение миграций
python manage.py migrate

# Запуск сервера разработки
python manage.py runserver
```

## Смена версии Python на Windows

```powershell
# Создание виртуального окружения с Python 3.11
py -3.11 -m venv .venv

# Активация виртуального окружения
.\.venv\Scripts\Activate.ps1

# Установка Django 4.0.8
python -m pip install Django==4.0.8

# Создание проекта Django в текущей папке
django-admin startproject base .
```

## Основные команды управления Django

```bash
# Запуск сервера разработки
python -m manage runserver

# Создание нового приложения shop
py -m manage startapp shop

# Создание суперпользователя
py -m manage createsuperuser

# Создание миграций после изменения моделей
py -m manage makemigrations

# Применение миграций к базе данных
py -m manage migrate
```

## Добавление записей в базу данных

### 1. Войти в Django shell

```bash
py -m manage shell
```

### 2. Импортировать модели

```python
from shop.models import Category, Course
```

### 3. Посмотреть все записи

```python
# Получить все курсы
Course.objects.all()

# Получить все категории
Category.objects.all()
```

### 4. Создать новую категорию

```python
new_category = Category(title="Programming")
new_category.save()
```

### 5. Проверить созданную запись

```python
# Получить id созданной категории
new_category.id

# Получить дату создания
new_category.created_at
```

### 6. Найти запись по primary key

```python
Category.objects.get(pk=1)
Category.objects.get(pk=1).title
```

### 7. Отфильтровать записи по названию

```python
Category.objects.filter(title="Programming")
Category.objects.filter(title="Programming")[0].title
```

### 8. Подготовить категорию для создания курса

```python
category = Category.objects.get(id=1)

# Получить все курсы этой категории
category.course_set.all()
```

### 9. Создать новый курс в этой категории

```python
category.course_set.create(
    title="Complete Python Guide",
    price=9.99,
    students_qty=100,
    reviews_qty=50,
)
```

### 10. Проверить созданный курс

```python
# Получить курс по primary key
Course.objects.get(pk=1)
```

### 11. Получить список названий всех курсов

```python
[course.title for course in Course.objects.all()]
```
