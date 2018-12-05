#!/usr/bin/env python
from tetpyclient import RestClient, MultiPartOption
import requests.packages.urllib3
from argparse import ArgumentParser
import json

CLUSTER_URL="https://andromeda-aus.cisco.com"
CRED_FILE="./cred.json"

CSV_FILE="./mytags.csv"
ROOT_SCOPE="Lab User 23"

parser = ArgumentParser("usage: push_tags.py")

parser.add_argument("-t", "--tag", dest="tag", help="Tag to be added / modified. Ex: quarantine=yes", required=True)
parser.add_argument("-i", "--ip", dest="ip", help="Add tag to this IP. Ex: 10.60.7.71", required=True)
args = parser.parse_args()

ip_value = args.ip
tag_field = args.tag.split('=')[0]
tag_value = args.tag.split('=')[1]


requests.packages.urllib3.disable_warnings()
rc = RestClient(CLUSTER_URL, credentials_file=CRED_FILE, verify=False)


req_payload = {'ip': ip_value, 'attributes': {tag_field: tag_value}}
resp = rc.post('/inventory/tags/' + ROOT_SCOPE, json_body=json.dumps(req_payload))


# Checking result
if resp.status_code == 200:
	print("Done!")
else:
	print("Error: HTTP status code is "+str(resp.status_code)+" and message is "+resp.content)
