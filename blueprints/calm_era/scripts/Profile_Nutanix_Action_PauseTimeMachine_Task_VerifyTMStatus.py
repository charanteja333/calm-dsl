
tm_status = "@@{TM_STATUS}@@"
expected_status = "PAUSED"

if tm_status != expected_status:
  print "Time Machine state(%s) is not in expected state(%s)" % (tm_status, expected_status) 
  exit(1)
  
print "Time Machine state(%s) is in expected state(%s)" % (tm_status, expected_status) 