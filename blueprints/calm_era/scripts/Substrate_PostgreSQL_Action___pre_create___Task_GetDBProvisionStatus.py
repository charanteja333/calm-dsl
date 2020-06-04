
# Set creds, headers, and URL
era_user = '@@{era_web_cred.username}@@'
era_pass = '@@{era_web_cred.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
url     = "https://@@{ERA_IP}@@/era/v0.8/operations/@@{OPERATION_ID}@@"
resp_out = {}

# Monitor the operation
for x in range(20):
  
  sleep(30)
  resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
  resp_out = json.loads(resp.content)
  print "Percentage Complete: {0}".format(resp_out['percentageComplete'])
  
  
  # If complete, break out of loop
  if resp_out['percentageComplete'] == "100" or resp_out['status'] == "5" :
    break    

# If the operation did not complete within 20 minutes, assume it's not successful and error out
if 'percentageComplete' not in resp_out or 'status' not in resp_out:
  exit(1)
elif resp_out['percentageComplete'] != "100" or resp_out['status'] != "5" :  
  exit(1)
 