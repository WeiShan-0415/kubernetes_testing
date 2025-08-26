from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='my_first_dag_gitsync',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    # Define a simple BashOperator task
    hello_task = BashOperator(
        task_id='hello_world',
        bash_command='echo "Hello from Airflow DAG synced via Git!"'
    )