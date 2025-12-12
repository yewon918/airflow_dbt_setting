from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime

def test_s3():
    hook = S3Hook(aws_conn_id='s3_conn')
    hook.load_string("Hello from Airflow", key="test/hello.txt", bucket_name="my-airflow-logs")

with DAG(
    dag_id="test_s3_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    PythonOperator(
        task_id="write_to_s3",
        python_callable=test_s3,
    )
