# Use ConfigMaps
Objective: Use ConfigMaps for environment variables and configuration files.

## Steps:
* Review config_map files
```bash
cat config_map_env.yaml
cat config_map_file.yaml
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

* Test app
Review config value
```bash
curl http://localhost:30000
```

Review env vars
```bash
curl -X 'GET' \
  'http://localhost:30000/env_vars' \
  -H 'accept: application/json'
```

# Cleanup
```bash
kubectl delete -f .
```