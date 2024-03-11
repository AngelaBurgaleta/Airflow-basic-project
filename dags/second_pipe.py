from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator



with DAG('dag2', start_date=datetime(2025, 1, 1),
         description='second DAG with bash and python operators', tags=['data_science'],
         schedule_interval='@daily', catchup=False):
    
        create_file = BashOperator(
        task_id="create_file",
        bash_command='echo "hello world" > ./dummy'
        )

        check_file_exist = BashOperator(
        task_id='check_file_exist',
        bash_command='test -f ./dummy'
        )

        read_file = PythonOperator(
                task_id='read_file', 
                python_callable=lambda: print(open ('./dummy', 'rb').read())
        )

        create_file >> check_file_exist >> read_file