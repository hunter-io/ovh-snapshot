import os
import sys

from client import create_client
from tabulate import tabulate

PROJECT_ID = os.environ.get('PROJECT_ID')

if PROJECT_ID is None:
  print('Please provide a PROJECT_ID')
  sys.exit(1)

client = create_client()
instances = client.get('/cloud/project/%s/instance' % PROJECT_ID)

instancesArray = []

for instance in instances:
  instancesArray.append([instance.get('name'), instance.get('id')])

print(tabulate(instancesArray, headers=['Name', 'ID']))
