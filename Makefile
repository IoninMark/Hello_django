install:
	poetry install

run:
	poetry run python manage.py runserver

run2:
	export DJANGO_SETTINGS_MODULE=hello_django.settings && \
	poetry run gunicorn hello_django.wsgi

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 hello-django

test:
	poetry run pytest

