# Courses Shop Django

A learning Django project for a simple online course shop. The app includes course and category models, a course listing page, basic templates, styles, and the Django admin panel.

## Tech Stack

- Python
- Django 4.0.8
- SQLite
- HTML / CSS
- Pipenv

## Features

- displays a list of courses on the main page;
- stores courses and categories in the database;
- connects each course to a category through `ForeignKey`;
- supports data management through Django admin;
- uses Django templates to render a courses table.

## Project Structure

```text
Courses-Shop-Django/
├── base/                  # Django project settings
├── shop/                  # courses app
│   ├── migrations/        # database migrations
│   ├── static/            # app CSS and static files
│   ├── templates/         # HTML templates
│   ├── models.py          # Category and Course models
│   ├── urls.py            # app routes
│   └── views.py           # app views
├── manage.py
├── Pipfile
├── Pipfile.lock
├── start.md
└── start.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/<username>/Courses-Shop-Django.git
cd Courses-Shop-Django
```

### 2. Install dependencies

Using Pipenv:

```bash
python -m pip install pipenv
python -m pipenv install
python -m pipenv shell
```

Or using a regular virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install Django==4.0.8
```

For Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install Django==4.0.8
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

After starting the server, the project will be available at:

```text
http://127.0.0.1:8000/
```

Django admin:

```text
http://127.0.0.1:8000/admin/
```

## Common Commands

```bash
# Run the development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

## Models

### Category

Represents a course category.

Fields:

- `title` - category name;
- `created_at` - creation date.

### Course

Represents a course that belongs to a category.

Fields:

- `title` - course title;
- `price` - course price;
- `students_qty` - number of students;
- `reviews_qty` - number of reviews;
- `category` - course category;
- `created_at` - creation date.

## Adding Sample Data in Django Shell

```bash
python manage.py shell
```

```python
from shop.models import Category, Course

category = Category.objects.create(title="Programming")

Course.objects.create(
    title="Complete Python Guide",
    price=9.99,
    students_qty=100,
    reviews_qty=50,
    category=category,
)

Course.objects.all()
```

## Routes

| URL | Description |
| --- | --- |
| `/` | course list |
| `/shop/` | course list |
| `/admin/` | Django admin panel |

## Note

This project was created for learning Django. The current settings are intended for local development: SQLite is used as the database, `DEBUG=True` is enabled, and the secret key is stored in `settings.py`. Before using this project in production, move sensitive values to environment variables and configure production security settings.
