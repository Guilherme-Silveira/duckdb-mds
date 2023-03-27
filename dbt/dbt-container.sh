#!/bin/bash

docker run --rm -it --mount type=bind,source=${PWD},target=/usr/app/dbt \
 --mount type=bind,source=${PWD}/profiles.yml,target=/root/.dbt/profiles.yml \
 --port 8080:8080 \
 --env-file ${PWD}/.env \
 --entrypoint bash  guisilveira/dbt-duckdb