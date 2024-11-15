
# Install go
```bash
sudo apt install golang-go -y
```
* Add go bin path to your shell
```bash
export PATH="$(go env GOPATH)/bin:$PATH"
```

# Install KIND
```bash
go install sigs.k8s.io/kind@v0.25.0
```
# Test kind
```bash
kind version
```

# Install Cluster
```bash
cat <<EOF > kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 9080
        hostPort: 9080
        protocol: TCP
EOF
```
**Note:** extraPortMapping is used to map ports to the cluster. This can be done only during the cluster creation. If you need to forward additional ports, you need to recreate the cluster

```bash
kind create cluster --config kind-config.yaml
kind get clusters
kubectl cluster-info
```

# Review the the KUBECONFIG file
```bash
cat ~/.kube/config
```


# Namespaces
* List namespaces
```bash
kubectl get namespaces
```

* List pods for 'kube-system' namespace
```bash
k get pods -n kube-system
```

* List pods for all namespace
```bash
k get pods -A
```

* Create namespace
```bash
kubectl create namespace myapp
```

* Alternavetly you can create namespace with yaml manifest
```bash
cat <<EOF > myapp2-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: myapp2
EOF

kubectl apply -f myapp2-namespace.yaml
```
## Delete namespace
```bash
kubectl delete namespace myapp
```

## Set default namespace
* By default kubectl uses a namespace with name 'default'. All commands are executed against this namespace unless you specify '-n namespace-name'
* You can specify new default namespace for the current context.
```bash
kubectl config set-context --current --namespace=myapp2
```
# PODs with imperative commands
* Run simple echo server 
```bash
kubectl run echo-server --image=ealen/echo-server --port=8080
```

* Wait POD condition to be Ready
```bash
kubectl wait --for=condition=Ready pod/echo-server --timeout=120s
```

* Expose port
```bash
kubectl expose pod echo-server --type=NodePort --port=9080 --target-port=8080
```