import os
import sys

from client import create_client
from notifier import notify

PROJECT_ID = os.environ.get('PROJECT_ID')
INSTANCES = os.environ.get('INSTANCES')
NUMBER_SNAPSHOTS_TO_KEEP = os.environ.get('NUMBER_SNAPSHOTS_TO_KEEP')

if PROJECT_ID is None or INSTANCES is None:
  print('Please provide a PROJECT_ID and a comma-separated list of INSTANCES')
  sys.exit(1)

if NUMBER_SNAPSHOTS_TO_KEEP is None:
  number_snapshots_to_keep = 3
else:
  number_snapshots_to_keep = int(NUMBER_SNAPSHOTS_TO_KEEP)

notify('run')

client = create_client()

# this will contain the identifier of each snapshot of each instance
snapshots_per_instances = dict()

for snapshot in client.get('/cloud/project/%s/snapshot' % PROJECT_ID):
  instance = snapshot.get('name')[:36]

  if instance in INSTANCES.split(','):
    snapshots_per_instances.setdefault(instance, []).append(snapshot.get('id'))


for instance in snapshots_per_instances:
  # creates a new array containing the oldest snapshots (they are returned by desc
  # creation date by the OVH API)
  snapshots_to_delete = snapshots_per_instances[instance][number_snapshots_to_keep:]

  for snapshot in snapshots_to_delete:
    client.delete('/cloud/project/%s/snapshot/%s' % (PROJECT_ID, snapshot))

    print('Scheduled deletion of snapshot %s' % snapshot)

notify('complete')

print('Finished scheduling the snapshots deletion')
