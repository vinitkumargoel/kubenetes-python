# Kubernetes Python

## Important commands

- **Run Program** = python run.py
- **Get list of Namespaces** = kubectl get namespaces
- **Delete Particular Namespaces** =  kubectl delete namespaces <NAMESPACE_NAME>
- **Get Roles in Namespace** = kubectl get role -n <NAMESPACE_NAME>
- **Get Role Bindings in Namespace** = kubectl get rolebindings.rbac.authorization.k8s.io -n <NAMESPACE_NAME>
- **Get Auth Token** = kubectl describe secret $(kubectl get secrets | grep ^default | cut -f1 -d ' ') | grep -E '^token' | cut - f2 -d':' | tr -d " "
- **Use User account to access namespace** = kubectl get pods --as="<USER_NAME>" --namespace="<NAMESPACE_NAME>"