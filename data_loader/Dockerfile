FROM debian:stable-slim

RUN apt update
RUN apt install -y iputils-ping python3-dev libpq-dev python3-pip
RUN python3 -m pip install psycopg2 click pyserial

ENTRYPOINT /root/run.sh
