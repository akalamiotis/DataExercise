Installation
============

This project is built using docker and docker-compose. Please first install docker, and then build and run the images using the commands below. 

1) Install Docker:

For Linux: https://docs.docker.com/install/linux/docker-ce/ubuntu/

2) Install Docker Compose:

https://docs.docker.com/compose/install/

Add your user to the docker group:

https://docs.docker.com/install/linux/linux-postinstall/


Running the Project
===================

In the first time build the project:
$ make build

Then to run the project:
$ make run

To import files form "sample_data" folder into PostgreSQL database:
$ make import_data


Additional available commands
=============================

Django migrations:
$ make makemigrations
$ make migrate

Django shell:
$ make shell

Access the project on: http://localhost:8000/