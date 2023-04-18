#!/bin/bash

python3 load_into_postgres.py &

python3 load_gse_into_postgres.py &

wait -n

exit $?

