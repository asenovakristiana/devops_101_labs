import json


def load_json_file(filename: str):
    with open(filename, 'r') as file:
        return json.loads(file.read())


config = load_json_file('02_config_file.json')
print(config.get('username'))