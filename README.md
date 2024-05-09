[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![mypy](https://img.shields.io/badge/mypy-checked-brightgreen.svg)](https://mypy.readthedocs.io/en/stable/)
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>
[![Static Badge](https://img.shields.io/badge/crispy--bootstrap4-2024.1-blue.svg)](https://pypi.org/project/crispy-bootstrap4/)
[![Static Badge](https://img.shields.io/badge/django--crispy--forms-2.1-blue.svg)](https://pypi.org/project/django-crispy-forms/)
[![Static Badge](https://img.shields.io/badge/social--auth--app--django-5.4.1-blue.svg)](https://pypi.org/project/social-auth-app-django/)

## Setup
Install the dependencies:

`pip install -r requirements.txt`

Make migrations:

`python manage.py makemigrations`

Migrate:

`python manage.py migrate`

## Setup Local Database
1.)Download Postgresql according to your operating system:https://www.postgresql.org/download/

2.)Open pgAdmin4( it will be automatically included when you download postgresql)

3.)Click Server and right click Databases, create new Database

4.)For keeping sensitive information about database, create .env file in your repository, add it to .gitignore.

5.) Your .env file should look like this:
`SECRET_KEY=django-insecure-728k0bs%91o$^sp%aa_ji@2fmtwpdk7r1na#*$%l2+%)7tnpo3
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432`

6.) Make migrations and migrate, your local postgresql database is ready.
## Run
`python manage.py runserver`

And navigate to `http://127.0.0.1:8000`.
