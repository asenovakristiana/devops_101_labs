# Ingress
Objective: Expose services using Ingress

## Steps:
* Review the offical NGINX controller definition
```bash
open https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

* Install NGINX ingress controller
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
``` 
* Change ingress controler NodePort
```bash
kubectl patch service ingress-nginx-controller -n ingress-nginx -p '{"spec": {"type": "NodePort", "ports": [{"port": 80, "nodePort": 30000, "protocol": "TCP", "targetPort": 80}]}}'
```

* Review pods, services and ingress manifests
```bash
cat pods.yaml
cat services.yaml
cat ingress.yaml
```

* Apply manifests
```bash
kubectl apply -f .
```

* Review ingress object
```bash
kubectl describe ingress my-apps-ingress
```
**Note:** In the events, you should see that nginx-ingress-controller is syncing this ingress resource. 
```
Normal  Sync    15m (x2 over 15m)  nginx-ingress-controller  Scheduled for sync
```

* Test connection to both apps
```bash
curl http://localhost:30000
curl http://localhost:30000/subpath
```

# Cleanup
```bash
kubectl delete -f .
```