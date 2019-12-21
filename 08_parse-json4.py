# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 08:51:37 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ptW0Bp1aAT9MJIdE6eFewvRBvuGPRQRC"

while True:
    orig = input("Ingrese el origen: ")
    if orig =="quit" or orig == "q":
        break
    dest = input("Ingrese el destino ")
    if dest =="quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")


