FROM apache/airflow:2.9.0-python3.10

USER airflow

# dbt + AWS 연동(필요 시) + 기타 유틸 설치
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir \
    dbt-core \
    dbt-spark \
    dbt-postgres 

USER root
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER airflow

ENV DBT_PROJECT_DIR=/opt/dbt/project
ENV DBT_PROFILES_DIR=/opt/dbt