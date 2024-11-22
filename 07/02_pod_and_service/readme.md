# Run echo-server (imperative commands)
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
kubectl get pods --selector=app=echo-server
```
**Note:** We will use this selector in the service to match the specific PODs.

# Create service
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

* Validate connection service
```bash
curl localhost:30000
```

* Read container logs
```bash
kubectl logs echo-server
```

# Clean up
```bash
kubectl delete pod echo-server
kubectl delete service echo-server
```


