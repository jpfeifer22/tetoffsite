#!/usr/bin/env python
# Imports
from tetpyclient import RestClient, MultiPartOption
import requests.packages.urllib3

CLUSTER_URL="https://andromeda-aus.cisco.com"
CRED_FILE="./cred.json"

CSV_FILE="./tags.csv"
ROOT_SCOPE="Lab User 23"

requests.packages.urllib3.disable_warnings()
rc = RestClient(CLUSTER_URL, credentials_file=CRED_FILE, verify=False)

# Get annotations csv (insert code to download annotations here)
resp = rc.download(CSV_FILE, '/assets/cmdb/download/' + ROOT_SCOPE)

# Checking result
if resp.status_code == 200:
    print("Annotations download successful!")
else:
    print("Error: HTTP status code is "+str(resp.status_code)+" and message is "+resp.content)
