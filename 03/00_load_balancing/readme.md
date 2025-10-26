# Run apps
* Run the following commands. This will create two web app processes and send them in background.
```bash
python app.py --port 9001 --name server1 &
python app.py --port 9002 --name server2 &
```

# Review the proxy config and run it
* **Note: ** we are using simple proxy implement in GOLang implemented for demo purposes
* Open new terminal
* Review the proxy config
```bash
cat config.yaml
```
* Run the proxy
```bash
./go-lb -config config.yaml
```

* Review the proxy logs for health checks

# Open new terminal and run curl
```bash
curl localhost:9000
curl localhost:9000
curl localhost:9000
curl localhost:9000
```