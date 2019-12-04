.PHONY: help
help: ## This help dialog.
help: help-display

.PHONY: build
build: ## Build the project
	docker-compose up -d --build

.PHONY: run
run: ## Run the project
	docker-compose up

.PHONY: makemigrations
makemigrations: ## Perform django makemigrations in containers.
	docker-compose run web python /code/manage.py makemigrations --noinput

.PHONY: migrate
migrate: ## Perform django migrate in containers.
	docker-compose run web python /code/manage.py migrate --noinput

.PHONY: shell
shell: ## Perform django migrate in containers.
	docker-compose run web python /code/manage.py shell

.PHONY: tests
tests: ## Perform django migrate in containers.
	docker-compose run web python /code/manage.py test

.PHONY: import_data
import_data: ## Load data into the database
	docker-compose run web python /code/manage.py import_data
