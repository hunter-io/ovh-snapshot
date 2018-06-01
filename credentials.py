import ovh

from client import create_client

client = create_client()

ck = client.new_consumer_key_request()
ck.add_recursive_rules(ovh.API_READ_WRITE, '/')

validation = ck.request()

print('Please visit %s to authenticate' % validation['validationUrl'])

input('Press Enter to continue')

print('Welcome %s, your consumerKey is "%s"' % (client.get('/me')['firstname'], validation['consumerKey']))
