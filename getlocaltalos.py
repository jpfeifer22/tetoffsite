#!/usr/bin/python

import json
import os
import sys
import time
import pprint
import time
import requests

url = "http://localhost:8080"

response = requests.request("GET", url)
#print response.text

for entry in response.text.split("\n"):
    if entry == "":
        continue
    print entry
