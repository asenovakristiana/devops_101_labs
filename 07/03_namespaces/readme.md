# Namespaces
* List namespaces
```bash
kubectl get namespaces
```

* List pods for 'kube-system' namespace
```bash
kubectl get pods -n kube-system
```

* List pods for all namespace
```bash
kubectl get pods -A
```

* Create namespace
```bash
kubectl create namespace myapp
```

* Delete namespace
```bash
kubectl delete namespace myapp
```

* Alternavetly you can create namespace with yaml manifest
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Namespace
metadata:
  name: myapp
EOF
```

* Set default namespace
**Note:** By default kubectl uses a namespace with name 'default'. All commands are executed against this namespace unless you specify '-n namespace-name'. You can also specify new default namespace for the current context.
```bash
kubectl config set-context --current --namespace=myapp
```