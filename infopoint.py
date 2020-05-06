#!/usr/bin/env python3
"""InfoPoint API Test"""

import json
import requests

from datetime import datetime, timedelta

config_file = 'infopoint.config.json'


# -- Convert JSON /Date()/ to datetime -------------------------------->
def json_date(json_date):
    sign = json_date[-7]

    if sign not in '+-' or len(date) == 13:
        millisec = int(date[6:-2])
    else:
        millisec = int(date[6:-7])
        hh = int(date[-7:-4])
        mm = int(date[-4:-2])
        if sign == '-': mm = -mm
        millisec += (hh * 60 + mm) * 60000

    last_updated = datetime(1970, 1, 1) \
        + timedelta(microseconds=millisec*1000)

    return last_updated  # use .strftime("%Y-%m-%d %H:%M:%S") for string


# -- __main__ --------------------------------------------------------->
with open(config_file) as config:
    config_vars = json.load(config)

infopoint_url = config_vars['InfoPoint']
get_visible_routes = config_vars['GetVisibleRoutes']
no_vehicle = config_vars['NoVehicle']

infopoint = requests.get(f'{infopoint_url}/{get_visible_routes}')
infopoint.close()

# -- Valid API Response ----------------------------------------------->
if infopoint.status_code == 200:
    routes = infopoint.json()
    for route in routes:
        if route['RouteId'] > 99: continue  # Skip specialty routes

        if route['Vehicles'] == []:
            route['Vehicles'] = no_vehicle

        route['StatusList'] = []
        for vehicle in route['Vehicles']:
            route['StatusList'].append(vehicle['DisplayStatus'])
        
        if 'Early' in route['StatusList']:
            status = 'Early'
        elif 'Late' in route['StatusList']:
            status = 'Late'
        elif 'On Time' in route['StatusList']:
            status = 'On Time'
        else:
            status = 'Unknown'

        print(f"{route['RouteId']:<3}: {status}")

# -- Invalid API Response --------------------------------------------->
else:
    print(f'Invalid response type detected! {infopoint.status_code}')