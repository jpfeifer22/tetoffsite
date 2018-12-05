#!/usr/bin/env python

from tetpyclient import RestClient
import requests.packages.urllib3
import json

CLUSTER_URL="https://andromeda-aus.cisco.com"
CRED_FILE="./cred.json"

MY_APP = "Siwapp Prod"

requests.packages.urllib3.disable_warnings()
rc = RestClient(CLUSTER_URL, credentials_file=CRED_FILE, verify=False)

resp = rc.get("/openapi/v1/applications")

if resp.status_code == 200:
    for app in json.loads(resp.content):
        if app['name'] == MY_APP:
            my_app_id = app['id']
        
    if not 'my_app_id' in vars():
        print(MY_APP+" Not found!")
    else:
        resp_policy = rc.get("/openapi/v1/applications/"+my_app_id+"/details")
        if resp_policy.status_code == 200:
            print(json.dumps(json.loads(resp_policy.content), indent=4, sort_keys=True))
        else:
            print("Error: HTTP status code is "+str(resp_policy.status_code)+" and message is "+resp_policy.content)

else:
	print("Error: HTTP status code is "+str(resp.status_code)+" and message is "+resp.content)
