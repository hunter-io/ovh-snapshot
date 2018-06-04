import os
import sys
import time

from client import create_client

PROJECT_ID = os.environ.get('PROJECT_ID')
INSTANCES = os.environ.get('INSTANCES')

if PROJECT_ID is None or INSTANCES is None:
  print('Please provide a PROJECT_ID and a comma-separated list of INSTANCES')
  sys.exit(1)

client = create_client()

for instance in INSTANCES.split(','):
  client.post('/cloud/project/%s/instance/%s/snapshot' % (PROJECT_ID, instance),
    snapshotName=instance + '-' + time.strftime('%Y%m%d-%H%M%S')
  )

  print('Scheduled snapshot of instance %s' % instance)
