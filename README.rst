Installation
============

This project supports docker. Please first install docker, and then build and run the images using the commands below. Exporting UID to environment is important, in order to run some containers using non-root privileges.

1) Install Docker
--------------

For Linux: https://docs.docker.com/install/linux/docker-ce/ubuntu/

2) Install Docker Compose
----------------------

For Linux click the "Linux" tab and follow the instructions:

https://docs.docker.com/compose/install/

Add your user to the docker group:

https://docs.docker.com/install/linux/linux-postinstall/


Running the Project
===================

In the first time build the project:
$ make build

Then to run the project:
$ make run

Access the project on: http://localhost:8000/