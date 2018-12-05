#!/usr/bin/env python

import json

from tetpyclient import RestClient
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
rc = RestClient("https://andromeda-aus.cisco.com", credentials_file="./cred.json", verify=False)

resp = rc.get("/openapi/v1/sensors")


print(resp.__dict__)

if resp.status_code == 200:
    print "good"
    print(json.dumps(json.loads(resp.content), indent=4, sort_keys=True))
else:
    print("Error: HTTP status code is "+str(resp.status_code)+" and message is "+resp.content)


