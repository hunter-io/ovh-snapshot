import os
import ovh

def create_client():
  return ovh.Client(
    endpoint=os.environ.get('ENDPOINT'),
    application_key=os.environ.get('APPLICATION_KEY'),
    application_secret=os.environ.get('APPLICATION_SECRET'),
    consumer_key=os.environ.get('CONSUMER_KEY'),
  )
