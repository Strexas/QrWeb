[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![mypy](https://img.shields.io/badge/mypy-checked-brightgreen.svg)](https://mypy.readthedocs.io/en/stable/)
[![PyPI version](https://badge.fury.io/py/Django.svg)](https://badge.fury.io/py/Django)
[![PyPI version](https://badge.fury.io/py/crispy-bootstrap4.svg)](https://badge.fury.io/py/crispy-bootstrap4)
[![PyPI version](https://badge.fury.io/py/django-crispy-forms.svg)](https://badge.fury.io/py/django-crispy-forms)
[![PyPI version](https://badge.fury.io/py/social-auth-app-django.svg)](https://badge.fury.io/py/social-auth-app-django)
## Setup
Create a virtual environment to install dependencies in and activate it:

`virtualenv --no-site-packages env`


`source env/Scripts/activate`

Then install the dependencies:

`pip install -r requirements.txt`

Don`t forget to migrate before start:

`python manage.py migrate`
## Run
`python manage.py runserver`

And navigate to `http://127.0.0.1:8000`.
