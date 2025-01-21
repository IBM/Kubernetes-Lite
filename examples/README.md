# Examples

| File Name | Short Description | Link |
|---|---|---|
| dynamic_create_update_delete_deployment.py | Pythonic copy of the client-go example | [Documentation](#create-update--delete-deployment-with-the-dynamic-client) |
| notebook.ipynb | Jupyter Notebook walkthrough of envtest & client | [Documentation](#kubernetes-lite-walkthrough-via-jupyter-notebook) |
| test_kubernetes.py | Pytest example using EnvTest and the [official Kubernetes client](https://github.com/kubernetes-client/python) | [Documentation](#pytest-example-using-envtest-and-the-official-kubernetes-python-client) |



# Create, Update & Delete Deployment with the Dynamic Client

This example is almost a direct copy of the [client-go](https://github.com/kubernetes/client-go/blob/master/examples/dynamic-create-update-delete-deployment/README.md) example of the same name. This demonstrates the fundamental operations for managing on Deployment resources, such as Create, List, Update and Delete using the kubernetes_lite client.


## Running this example

Make sure you have a Kubernetes cluster and `kubectl` is configured:
```
kubectl get nodes
```

Install the kubernetes_lite package on your workstation:

```
# Remote Install
pip3 install kubernetes_lite
# Local Install
pip3 install -e "."
```

Now, run this application on your workstation with your local kubeconfig file:

```
python3 dynamic_create_update_delete_deployment.py
# or specify a kubeconfig file with flag
python3 dynamic_create_update_delete_deployment.py -kubeconfig=$HOME/.kube/config
```

Running this command will execute the following operations on your cluster:

1. **Create Deployment:** This will create a 2 replica Deployment. Verify with
   `kubectl get pods`.
2. **Update Deployment:** This will update the Deployment resource created in
   previous step by setting the replica count to 1 and changing the container
   image to `nginx:1.13`. You are encouraged to inspect the retry loop that
   handles conflicts. Verify the new replica count and container image with
   `kubectl describe deployment demo`.
3. **List Deployments:** This will retrieve Deployments in the `default`
   namespace and print their names and replica counts.
4. **Delete Deployment:** This will delete the Deployment object and its
   dependent ReplicaSet resource. Verify with `kubectl get deployments`.

Each step is separated by an interactive prompt. You must hit the
<kbd>Return</kbd> key to proceed to the next step. You can use these prompts as
a break to take time to run `kubectl` and inspect the result of the operations
executed.

You should see an output like the following:

```
Creating deployment...
Created deployment "demo-deployment".
-> Press Return key to continue.
Updating deployment...
Updated deployment...
-> Press Return key to continue.
Listing deployments in namespace "default":
 * demo-deployment (1 replicas)
-> Press Return key to continue.
Deleting deployment...
Deleted deployment.
```

## Cleanup

Successfully running this program will clean the created artifacts. If you
terminate the program without completing, you can clean up the created
deployment with:

    kubectl delete -n default deploy demo-deployment

## Troubleshooting

If you are getting the following error, make sure Kubernetes version of your
cluster is v1.13 or higher in `kubectl version`:

    panic: the server could not find the requested resource


# Kubernetes Lite Walkthrough Via Jupyter Notebook

This example walks through using the kubernetes_lite library with a jupyer notebook. In addition to the client
operations described above, this notebook also showcases using `envtest` to start a cluster.

## Running this example

Install jupyter notebook and kubernetes_lite package on your workstation:

```
# Jupyter Install
pip3 install jupyter
# Remote Kubernetes Lite Install
pip3 install kubernetes_lite
# Local Kubernetes Lite Install
pip3 install -e "."
```

Start an instance of jupyter notebook in the examples directory

```
python3 -m jupyter notebook
```

Open up the `notebook.ipynb` file.

Execute the cells in the notebook from top to bottom. There is no need for a cluster connection since this notebook will handle starting an envtest instance 

## Troubleshooting

If you are getting the following error, make sure Kubernetes version of your
cluster is v1.13 or higher in `kubectl version`:

```python
kubernetes_lite.errors.UnknownError: no matches for kind "deployment" in version "apps/v1"
```

If you are getting the following error, the try to download the envtest binaries
before running the example e.g. `python3 -m kubernetes_lite.setup_envtest use`

```python
RuntimeError: unable to start control plane itself: failed to start the controlplane. retried 5 times: fork/exec etcd: no such file or directory
```


## Cleanup

Successfully running this program will correctly stop the envtest server.
If you terminate the program without completing, or an error occurs you can 
ensure all envtest subprocesses have been killed with:

```bash
pkill -9 -f "kubebuilder"
```



# Pytest Example using EnvTest and the Official Kubernetes Python Client

This example walks through using the EnvTest module with pytest to test the official [kubernetes](https://github.com/kubernetes-client/python) library. This example showcases using both the kubernetes CoreV1Api and DynamicClient classes with envtest

## Running this example

Install kubernetes_lite, kubernetes, and pytest on your local machine

```
# Kubernetes Install
pip3 install kubernetes
# Pytest Install
pip3 install pytest
# Remote Kubernetes Lite Install
pip3 install kubernetes_lite
# Local Kubernetes Lite Install
pip3 install -e "."
```

Run pytest against this example

```
python3 -m pytest test_kubernetes.py
```

You should see the following output from pytest:
```bash
❯ python3 -m pytest test_kubernetes.py
=============================================== test session starts ===============================================
platform darwin -- Python 3.11.5, pytest-8.3.2, pluggy-1.5.0
rootdir: <>
configfile: pyproject.toml
plugins: cov-5.0.0, anyio-4.8.0, typeguard-2.13.3, timeout-2.3.1
collected 2 items                                                                                                 

test_kubernetes.py ..                                                                              [100%]

================================================ 2 passed in 5.17s ================================================
```

## Troubleshooting

If you are getting the following error, the try to download the envtest binaries
before running the example e.g. `python3 -m kubernetes_lite.setup_envtest use`

```python
RuntimeError: unable to start control plane itself: failed to start the controlplane. retried 5 times: fork/exec etcd: no such file or directory
```

## Cleanup

Successfully running this program will correctly stop the envtest server.
If you terminate the program without completing, or an error occurs you can 
ensure all envtest subprocesses have been killed with:

```bash
pkill -9 -f "kubebuilder"
```