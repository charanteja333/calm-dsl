# Set creds and headers
era_user = '@@{era_web_cred.username}@@'
era_pass = '@@{era_web_cred.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Cluster ID
url     = "https://@@{ERA_IP}@@/era/v0.8/auth/validate?token=true&expire=15"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "TOKEN={0}".format(json.loads(resp.content)['token'])