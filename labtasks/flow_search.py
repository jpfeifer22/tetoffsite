#!/usr/bin/env python
from tetpyclient import RestClient
import json
import requests.packages.urllib3
from datetime import datetime, timedelta

CLUSTER_URL="https://andromeda-aus.cisco.com"
CRED_FILE="./cred.json"

### Define SCOPE_NAME, start, and end variables here

###

requests.packages.urllib3.disable_warnings()
rc = RestClient(CLUSTER_URL, credentials_file=CRED_FILE, verify=False)


req_payload = {
        "t0": start.strftime("%Y-%m-%dT%H:%M:%S-0000"),
        "t1": end.strftime("%Y-%m-%dT%H:%M:%S-0000"),
	"limit": 8,
	"filter": {},
        "scopeName": SCOPE_NAME
}

resp = rc.post("<ENDPOINT>", json_body=json.dumps(req_payload))

if resp.status_code == 200:
	print(json.dumps(json.loads(resp.content), indent=4, sort_keys=True))
else:
        print("Error: HTTP status code is "+str(resp.status_code)+" and message is "+resp.content)
