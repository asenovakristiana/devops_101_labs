# Use Secrets
Objective: Use Secrets to deliver sensitive configuration files

## Steps:
* Review secret file
```bash
cat secret.yaml
```

Secrets values are store in base64 format. In order to convert the real value of your secret to base64 you can use this command.
```bash
echo -n "mypassword" | base64  
```

* Review pod manifest
Rivew how the environment variables and config.yaml files are presented to the container
```bash
cat pod.yaml
```

* Apply manifests
```bash
kubectl apply -f .
```

* Review env vars
```bash
curl -X 'GET' \
  'http://localhost:30000/env_vars' \
  -H 'accept: application/json'
```

# Cleanup
```bash
kubectl delete -f .
```