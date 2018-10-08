# Kubernetes PodOperator
## Running the KubernetesPodOperator on Airflow 1.9

The KubernetesPodOperator spins up a pod to run a Docker container in. If you are running Airflow on Kubernetes, it is preferable to do this rather than use the DockerOperator.

This tutorial is for anyone using Airflow 1.9 and would like to use the KubernetesPodOperator without upgrading their version of Airflow.

It assumes a Dockerized Airflow setup (in this case, the Astronomer Setup), but should apply to any Airflow set up.


1. Create a Service Account.

Create a service account tied to a role that allows `create`, `get` and `watch` on pods, and `get` on `pods/logs`. Note that any task could potentially take these same actions on an arbitrary pod in the same namespace, assuming it could guess a name correctly, since it cannot list.

**Note:** If you are using this on Astronomer's Cloud Airflow, the service account is preconfigured to work in the cluster and you can skip this step. 

2. Fork the code found in this repository.

This repo contains all the necessary Kubernetes specific Airflow plugins with the right import paths.

3. Set `in_cluster` to `True`.

This will tell your task to look inside the cluster for the Kubernetes config. In this setup, the workers are tied to role with the right privledges in the cluster.

**Note**: If you are using this on Astronomer's Cloud Airflow, your namespace will be `astronomer-cloud-DOMAIN` (e.g. astronomer-cloud-frigid-vacuum-0996). 

4. Run an example.

Run the attached Ubuntu example to ensure that everything works as expected.
