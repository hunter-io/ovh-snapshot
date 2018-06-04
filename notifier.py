import os
import urllib.request

CRONITOR_URL = os.environ.get('CRONITOR_URL')

def notify(action):
  if CRONITOR_URL is None:
    return

  urllib.request.urlopen('%s/%s' % (CRONITOR_URL, action))
