# Postgres_RP_GUI
Server based GUI for the UCI Rocket Project

StartupCommands:

install docker and docker compose
[pull repo]
>CD Prometheus_GUI/docker-compose
>docker compose build
>docker compose up
>docker compose down(to shut down)

Docker Commands:

Get bash terminal into postgres container: docker exec -u postgres -it [container_id] bash


Grafana URL: http://localhost:3000/

Grafana-Postgres Datasource Config:
Host: localhost:5432
database: database_name_here
user: postgres
password: postgres
TLS/SSL Mode: disable
NOTE: table must have a timestamp value to be displayed
