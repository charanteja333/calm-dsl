
# Set creds, headers, and URL
era_user = '@@{era_web_cred.username}@@'
era_pass = '@@{era_web_cred.secret}@@'
tm_id = '@@{TM_ID}@@'

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

url = "https://@@{ERA_IP}@@:8443/era/v0.8/tms/%s/status?status=paused" % tm_id
resp_out = {}

# Get time machine id
resp = urlreq(url, verb='PATCH', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Resp Code", resp.status_code

if resp.status_code != 200:
  exit(1)
