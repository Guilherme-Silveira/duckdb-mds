FROM apache/superset:2.1.0

ENV PATH=$PATH:/app/superset_home/.local/bin/

ENV SUPERSET_SECRET_KEY=2Qr2oIHtQyxEArR81HoXsg3/9TMw0xpbxGBzsRoM1niFkfNlSsYN6w9/

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

RUN python -c 'import duckdb; con = duckdb.connect(database="/app/superset_home/abc.db", read_only=False); con.execute("INSTALL 'httpfs';"); con.execute("LOAD 'httpfs';")'
