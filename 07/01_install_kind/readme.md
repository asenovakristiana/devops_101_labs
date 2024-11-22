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


# Install metrics-server
Metrics Server is a scalable, efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines.  

Metrics Server collects resource metrics from Kubelets and exposes them in Kubernetes apiserver through Metrics API for use by ubectl kubectl top, making it easier to debug applications. Metrics API can also be accessed by Horizontal Pod Autoscaler and Vertical Pod Autoscaler.

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
```