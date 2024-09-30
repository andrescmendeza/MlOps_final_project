
## Informations

* Based on Python (3.7-slim-buster) official Image [python:3.7-slim-buster](https://hub.docker.com/_/python/) and uses the official [Postgres](https://hub.docker.com/_/postgres/) as backend and [Redis](https://hub.docker.com/_/redis/) as queue
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)

## Installation

Pull the image from the Docker repository.

    docker pull puckel/docker-airflow


Up the environmet
    docker-compose -f ./docker-compose.yml up -d

Stop the environmet: 
docker-compose -f ./docker-compose.yml down 

Create .env file locally,  example:

        POSTGRES_USER=airflow
        POSTGRES_PASSWORD=airflow
        POSTGRES_DB=airflow
        MYSQL_PASS=root
        SMTP_HOST=smtp.gmail.com
        EMAIL=correo@correo.com
        EMAIL_PASS=pass
        SMTP_MAIL_FROM= Magdalena-SAS

Enter airflow http://localhost:8080/admin/
Create the connection to the database name: mag_db_conn, Mysql: host, Schema: Magdalena_DB
Activate the workflow

Copy a Ventas file to the ip_files folder, you can choose any file from the folder ventas_files

Run the DAG workflow
