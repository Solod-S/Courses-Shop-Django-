# Начало работы с проектом Courses-Shop-Django

## Установка и настройка окружения

```bash
# Установка Pipenv (менеджер виртуального окружения)
python -m pip install pipenv

# Установка Django 4.0.8
python -m pipenv install django==4.0.8

# Активация виртуального окружения
python -m pipenv shell

# Получить полный путь к виртуальной среде
python -m pipenv --venv
```

> Пример пути к виртуальной среде:
> `C:\Users\Sergey\Documents\test\Courses-Shop-Django-\.venv\Scripts\python.exe`

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
# Создание нового проекта Django с именем base
django-admin startproject base .
```

## Смена версии Python

```bash
# Создание виртуального окружения с Python 3.11
py -3.11 -m venv .venv

# Активация виртуального окружения
.\.venv\Scripts\Activate.ps1

# Установка Django 4.0.8
python -m pip install Django==4.0.8

# Создание проекта Django
django-admin startproject base .
```

## Основные команды управления

```bash
# Запуск сервера разработки
python -m manage runserver

# Создание нового приложения shop
py -m manage startapp shop

# Создание суперпользователя
py -m manage createsuperuser

# Создание миграций на основе изменений моделей
py -m manage makemigrations

# Применение миграций к базе данных
py -m manage migrate
```
