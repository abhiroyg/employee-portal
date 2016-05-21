## Steps I did to achieve the current state of code.
    pip uninstall django
    pip install django # This should install 1.9.6
    django-admin startproject eportal
    cd eportal
    python manage.py startapp users

1. Write code given in [Django tutorial - Part 1](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)
1. Create a database and store its details in `eportal/eportal/settings.py`.
1. Run `python manage.py migrate` in outer `eportal`.
1. Write models in `eportal/users/models.py`.
