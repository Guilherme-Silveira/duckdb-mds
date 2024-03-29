#!/bin/bash

docker run --rm -it --mount type=bind,source=${PWD},target=/usr/app/dbt \
 --name dbt-duckdb \
 --mount type=bind,source=${PWD}/profiles.yml,target=/root/.dbt/profiles.yml \
 -p 8080:8080 \
 --env-file ${PWD}/.env \
 --entrypoint bash  guisilveira/dbt-duckdb