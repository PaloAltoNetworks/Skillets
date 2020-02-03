import json
import sys
import time
import os

username = os.environ.get('username', 'not found!')
secret = os.environ.get('secret', 'not found!')

output = dict()
output['output_example'] = dict()
output['output_example']['captured_username'] = username
output['output_example']['captured_secret'] = secret

# pretend we are doing something
z = 1
while z < 5:
    time.sleep(1)
    z = z + 1

# print out structured json as str back to user
print(json.dumps(output))

sys.exit(0)
