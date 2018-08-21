
from airflow import DAG
from datetime import datetime, timedelta
from plugins.operators import kubernetes_pod_operator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('example_kubernetes_pod',
          schedule_interval='@once',
          default_args=default_args)

with dag:
    k = kubernetes_pod_operator.KubernetesPodOperator(
        namespace='datarouter',
        image="ubuntu:16.04",
        cmds=["bash", "-cx"],
        arguments=["echo", "10", "echo pwd"],
        labels={"foo": "bar"},
        name="airflow-test-pod",
        in_cluster=True,
        task_id="task-two",
        get_logs=True,
        dag=dag)
