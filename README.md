# Postgres_RP_GUI
Server based GUI for the UCI Rocket Project

StartupCommands:

1. install docker and docker compose
2. pull repo
3. cd Prometheus_GUI/docker-compose
4. docker compose build
5. docker compose up
6. docker compose down(to shut down)

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

TO APPLY CHANGES IN /sql/init.sql, volumes need to be removed:  
docker-compose down --volumes
