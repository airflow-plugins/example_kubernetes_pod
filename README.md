# Kubernetes PodOperator
Running the KubernetesPodOperator on Airflow 1.9

The KubernetesPodOperator spins up a pod to run a Docker container in. If you are running Airflow on Kubernetes, it is preferable to do this rather than use the DockerOperator.

This tutorial is for anyone using Airflow 1.9 and would like to use the KubernetesPodOperator without upgrading their version of Airflow.

It assumes a Dockerized Airflow setup (in this case, the Astronomer Setup), but should apply to any Airflow set up.
