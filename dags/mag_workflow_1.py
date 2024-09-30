
"""
@author: andrescmendeza
Sales and Billing Providers workflow for Magdalena SAS
"""

from airflow import DAG # type: ignore
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator # type: ignore
from airflow.operators.python_operator import PythonOperator # type: ignore
from airflow.operators.mysql_operator import MySqlOperator # type: ignore

from pre_processing import pre_process
from pre_process import process_data

default_args={"owner":"airflow","start_date":datetime(2024,9,29)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily') as dag:
    
    check_file = BashOperator(
        task_id="check_file",
        bash_command="shasum ~/ip_files/ventas.csv",
        retries = 2,
        retry_delay=timedelta(seconds=15))
    
    pre_process = PythonOperator(
        task_id = "pre_process",
        python_callable = pre_process
    )

    agg = PythonOperator(
        task_id = "agg",
        python_callable = process_data
    )

    create_table = MySqlOperator(
        task_id="create_table",
        mysql_conn_id="mag_db_conn",
        sql="CREATE table IF NOT EXISTS load_ventas (id_prod varchar(10) NULL, cant varchar (3) NULL, fecha_ven varchar (10) NULL, cliente varchar (10) NULL, despacho varchar(1) NULL)"
    )
    

    load_ventas_table = MySqlOperator(
        task_id="load_ventas_table",
        mysql_conn_id="mag_db_conn",
        sql="LOAD DATA INFILE '/var/lib/mysql-files/final.csv' INTO TABLE load_ventas FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS; "
    )

    check_file >> pre_process >> agg >> create_table >> load_ventas_table