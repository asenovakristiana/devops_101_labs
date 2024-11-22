# Build application
* Enter my-app directory
```bash
cd my-app
```
* build application image
```bash
docker build . -t my-app
```

* Enter parent directory
```bash
cd ../
```

# Load image to KIND cluster
**Note:** Usually you will reference images from public or private registries. However, now will copy the local docker image to the KIND cluster to avoid installation and configuration of registry.
```bash
kind load docker-image my-app
```

# Create POD and Service
* Review POD manifest
```bash
cat pod.yaml
```

* Apply POD manifest
```bash
kubectl apply -f pod.yaml
```

* Review Service manifest
```bash
cat service.yaml
```

* Apply POD manifest
```bash
kubectl apply -f service.yaml
```

# Simulate problems
We will simulate some problems with workload see how kubernetes will restart the container.
## Simulate probes health check failing
```bash
curl -X 'PUT' \
  'http://localhost:30000/fail' \
  -H 'accept: application/json'
```
### Get pod details
```bash
kubectl get pods
```

### You should see something like this:
```bash
NAME         READY   STATUS    RESTARTS     AGE
my-app-pod   0/1     Running   1 (3s ago)   52m
```
Check the RESTARTS column and you should see 1 (...). If you don't see restarts, you may need to execute the command few times.

### Check POD events and Last Status
```bash
kubectl describe pod my-app-pod
```

# Simulate memory leak
```bash
curl -X 'PUT' \
  'http://localhost:30000/simulate-memory-leak' \
  -H 'accept: application/json'
```

# Simulate CPU stress
```bash
curl -X 'PUT' \
  'http://localhost:30000/simulate-cpu-stress' \
  -H 'accept: application/json'
```