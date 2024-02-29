postgres:
	docker run --name revista_pg -p 5439:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:16-alpine

createdb:
	docker exec -it revista_pg createdb --username=root --owner=root revista

dropdb:
	docker exec -it revista_pg dropdb revista

server:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

docker_build:
	docker-compose build

docker_postgres:
	docker-compose up -d postgres

docker_server:
	docker-compose up -d web

down_all:
	docker-compose down

docker_migrate:
	docker-compose exec web python manage.py migrate --noinput

docker_createsuperuser:
	docker-compose exec web python manage.py createsuperuser

.PHONY:
	postgres createdb dropdb server migrate makemigrations docker-migrate docker-createsuperuser
