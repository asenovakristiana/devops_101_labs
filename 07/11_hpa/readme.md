# Horizontal Pod Autoscaling
Objective: Demonstrate HPA scaling pods based on CPU usage.

## Steps:
* Review manifests
```bash
cat deployment.yaml
cat hpa.yaml
cat service.yaml
```
* Apply manifests
```bash
kubectl apply -f .
```

* Check HPA object
```bash
kubectl get hpa
```
**Note:** You should see MINPODS:1 MAXPODS:3 and RELICAS:1

* Simulate load
```bash
curl -X 'PUT' \
  'http://localhost:30000/simulate-cpu-stress' \
  -H 'accept: application/json'
```

* Check HPA object in new terminal
```bash
kubectl get hpa
```
**Note:** Repeat this tasks on every 10 seconds until you see REPLICAS:3

# Cleanup
```bash
kubectl delete -f .
```