# Troubleshooting Containers
Objective: Demonstrate debugging using kubectl exec and kubectl debug.

# Steps:
* Create a simple pod.

* Use kubectl exec to run commands in a container
```bash
kubectl exec -it troubleshoot-pod -- /bin/bash
```
This will start a bash shell in the container and should see a prompt like this: root@troubleshoot-pod:/app#
Every command that you execute in this shell is executed in the container context.

Execute ps command to list the processes
```bash
ps ax
```

Now lets execute a command that is not available in the image
```bash
ping 8.8.8.8
```
You will receive and error: bash: ping: command not found

Dettach from the container interactive shell with exit or CTRL+D


* Use kubectl debug to troubleshoot with a debug container
This brings another container in the same pod. Since all containers in POD share the same namespaces (e.g. PID, Networking, IPC, etc.), you can execute troobleshooting comamnds that are available in the image.
```bash
kubectl debug -it troubleshoot-pod --image=busybox --target=my-app-container
```

In the new shell execute ping
```bash
ping 8.8.8.8
```

* Use kubectl to forward local traffic to container that is not exposed
This is useful for some troubleshooting tricks. 
```bash
kubectl port-forward pod/troubleshoot-pod 2000:8000
```
Now you can access the application on local port 2000 util you run CTRL+C or close the terminal.  
Open new terminal and execute
```bash
curl http://localhost:2000
```

# Cleanup
```bash
kubectl delete -f .
```