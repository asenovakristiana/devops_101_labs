import os

username = os.environ.get('USERNAME')
if username:
    print(username)
else:
    print("Environment variable 'USERNAME' is not provided!")