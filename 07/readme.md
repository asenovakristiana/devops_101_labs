# Prerequsities
* Ensure you have compleated module 6
* You need to have docker up and running

# KIND Instalation
## Install go
```bash
sudo apt install golang-go -y
```

* Add go bin path to your shell
```bash
export PATH="$(go env GOPATH)/bin:$PATH"
```

## Install KIND executable
```bash
go install sigs.k8s.io/kind@v0.25.0
```

## Test kind
```bash
kind version
```

# Create KIND Cluster
```bash
cat <<EOF > kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 30000
        hostPort: 30000
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
kubectl run echo-server -l app=echo-server --port=5678 --image=hashicorp/http-echo -- -text="hello world"
```

* Wait echo-server POD condition to be Ready
```bash
kubectl wait --for=condition=Ready pod/echo-server --timeout=120s
```

* Review POD description
```bash
kubectl describe pod echo-server
```

* Test selector
```bash
kubectl get pods --selector=run=echo-server
```

* Create NodePod service on nodePort 30000 to echo-server pod 5678
```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: echo-server
spec:
  type: NodePort
  selector:
    app: echo-server
  ports:
    - protocol: TCP
      port: 5678          # Port on the Service
      targetPort: 5678    # Port on the Pod
      nodePort: 30000     # Specific NodePort
EOF
```

* Validate connection to echo server
```bash
curl localhost:30000
```
