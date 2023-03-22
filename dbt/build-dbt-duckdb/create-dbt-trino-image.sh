#!/bin/bash

docker build --tag guisilveira/dbt-duckdb \
  --target dbt-third-party \
  --build-arg dbt_third_party=dbt-duckdb \
  --build-arg dbt_core_ref=dbt-core@1.2.latest \
  .
