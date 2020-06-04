# Set creds, headers, and URL
era_user = '@@{era_web_cred.username}@@'
era_pass = '@@{era_web_cred.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
url     = "https://@@{ERA_IP}@@:8443/era/v0.8/tms/@@{TM_ID}@@/new"
resp_out = {}


payload = """
{
    "name":"@@{NEW_TM_NAME}@@",
    "description":"era_pg_db_tm_@@{calm_unique}@@",
    "id":"@@{TM_ID}@@",
    "slaId":"@@{SLA_ID}@@",
    "schedule":{
        "snapshotTimeOfDay":{
            "hours": @@{SCHEDULE_HOURS}@@,
            "minutes": @@{SCHEDULE_MINUTES}@@,
            "seconds": @@{SCHEDULE_SECONDS}@@
        },
        "continuousSchedule":{
            "enabled":true,
            "logBackupInterval": @@{LOG_CATCHUP_INTERVAL_IN_MINUTE}@@,
            "snapshotsPerDay": @@{SNAPSHOT_PER_DAY}@@
        },
        "weeklySchedule":{
            "enabled":true,
            "dayOfWeek":"@@{DAY_OF_WEEK}@@"
        },
        "monthlySchedule":{
            "enabled":true,
            "dayOfMonth":@@{DAY_OF_MONTH}@@
        },
        "quartelySchedule":{
            "enabled":true,
            "startMonth":"@@{QUARTER_START_MONTH}@@",
            "dayOfMonth": @@{DAY_OF_MONTH}@@
        },
        "yearlySchedule":{
            "enabled":false,
            "dayOfMonth":31,
            "month":"DECEMBER"
        }
    },
    "tags":[]
}
"""

# Update Time Machine
resp = urlreq(url, verb='PATCH', auth='BASIC', user=era_user, passwd=era_pass, params=payload, headers=headers)
resp_out = json.loads(resp.content)
print resp_out
  
if "status_code" in resp_out and  resp_out["status_code"] != 200:
  print "Time machine update is failed for @@{TM_NAME}@@"
  exit(1)
  

  
