import requests
from requests_oauthlib  import OAuth1

url = u'https://api.twitter.com/1/account/settings.json'

client_key = u'...'
client_secret = u'...'
resource_owner_key = u'...'
resource_owner_secret = u'...'

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')
r = requests.get(url, auth=headeroauth)

queryoauth = OAuth1(client_key, client_secret,
                    resource_owner_key, resource_owner_secret,
                    signature_type='query')
r = requests.get(url, auth=queryoauth)

bodyoauth = OAuth1(client_key, client_secret,
                   resource_owner_key, resource_owner_secret,
                   signature_type='body')

r = requests.post(url, auth=bodyoauth)