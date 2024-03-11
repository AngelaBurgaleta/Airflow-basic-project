from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_a():
    print('hi from task a')

def print_b():
    print('hi from task b')

with DAG('my_dag', start_date=datetime(2025, 1, 1),
         description='A simple tutorial DAG', tags=['data_science'],
         schedule_interval='@daily', catchup=False):
    
    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b)

    task_a >> task_b