# Create python venv and install dependencies
```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Create NewRelic account and get token
Go to new relic site and create account (Get Started for free)

# Create EC2 instances from Lab 10
Go to lab 10 terraform demo and tofu apply

# Install new relic collection
ansible-galaxy install newrelic.newrelic_install

# Test locally the container (This optional and it is just for testing)
```bash
docker run \
-e NEW_RELIC_LICENSE_KEY=your-license-key \
-e NEW_RELIC_APP_NAME="MyApiApp" \
-p 8000:8000 -it --rm --name  my-api-app my-api-app:latest
```

# Update playbook NEW_RELIC_API_KEY
* Get infrastructure agent key from NewRelic
* Update variable NEW_RELIC_API_KEY: SETAPIKEY

# Run ansible
```
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook playbook -i dynamic_inventory --private-key=$HOME/.ssh/id_rsa_tofu
```

# Review NewRelic account
Go to new relic site and review Logs, APM & Services
