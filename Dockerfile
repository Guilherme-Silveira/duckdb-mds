FROM apache/superset:latest

ENV PATH=$PATH:/app/superset_home/.local/bin/

COPY ./import_datasources.yaml /app/import_datasources.yaml

RUN superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

RUN superset db upgrade && superset init

RUN superset import_datasources -p /app/import_datasources.yaml

RUN pip install duckdb-engine duckdb dbt-duckdb==1.2.3
