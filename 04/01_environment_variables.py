import os

nickname = os.environ.get('NICKNAME')
if nickname:
    print(nickname)
else:
    print("Environment variable 'NICKNAME' is not provided!")