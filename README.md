# E-commerce Store Django Web
Build an E-commerce Store with Django

## Technologies used in applications
- [Python 3.9](https://docs.python.org/3.9/)
- [Django 4.1.4](https://docs.djangoproject.com/en/4.1/)

## How to run the application
### Copy `.env.sample` into `.env`
**Note**:
1. Overriding all the credentials are **required**.
2. `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` must be from a valid gmail account.
3. Check the `Setting-up-2FA-and-creating-an-app-password.pdf` for creating email app password tutorial.

### Setting up the pre-commit package
- Create new file `.pre-commit-config.yaml`
- Copy content from `.pre-commit-config.example` to `.pre-commit-config.yaml`
- Adjust the `files` directory as needed, example given on `.pre-commit-config.example`
- Run command `pre-commit install`
- Commit changes as usual

#### Pre-commit git hook scripts checks:
The scripts will run automatically with config on .pre-commit-config.yaml.
Hooks that currently actives:
- end-of-file-fixer
- trailing-whitespace
- black
- flake8

### Create Super User
```
python manage.py createsuperuser
```

## Accessing the apps using local browser
### Starting up the local server
```
python manage.py runserver
```
### Admin url
```
http://localhost:8000/admin/
```
### Index page url
```
http://localhost:8000/
```
