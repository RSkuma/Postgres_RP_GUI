#!/bin/bash

python3 /root/load_into_postgres.py &

python3 /root/load_gse_into_postgres.py &

wait -n

exit $?

