# ReplicaSet with Service
Objective: Create a ReplicaSet to ensure multiple replicas of a pod are running and expose them using a Service.

## Steps:
* Review replicaset.yaml manifest
```bash
cat replicaset.yaml
```

* Create a ReplicaSet to manage pod replicas
```bash
kubectl apply -f replicaset.yaml
```

* Review current pods
```bash
kubectl get pods
```
**Notes:** You should see 3 pods with random suffix (e.g. -8mzph)

* Simulate pod remove
In case something goes wrong with any of the pods (e.g. node failure), the kubernetes scheduler will immediately try to recover the replicaset in desired state.  

Replace -XXXXX with one of the random suffixes
```bash
kubectl delete pod my-app-replicaset-XXXXX
```

* Review current pods
```bash
kubectl get pods
```
**Notes:** You should see again 3 pods with random suffix and the age of one of them will be just few seconds.

* Create a Service to expose the pods to external traffic.
```bash
kubectl apply -f service.yaml
```

* Check service endpoints
```bash
kubectl describe service my-app-service | grep Endpoints
```
**Note:** You will see three endpoints in the list. Each endpoint will route traffic to the specific POD.

* Test load balancing
```bash
curl http://localhost:30000
curl http://localhost:30000
curl http://localhost:30000
curl http://localhost:30000
curl http://localhost:30000
curl http://localhost:30000
```
**Note:** If you look carefully, you will find that the hostname in the responses is different. The service

* Cleanup
Remove all kubernetes objects created by this lab
```bash
kubectl delete -f .  
```