#!/usr/bin/env python3
"""InfoPoint API Test"""

import json
import requests

config_file = 'infopoint.config.json'

with open(config_file) as config:
    config_vars = json.load(config)

infopoint_url = config_vars['InfoPoint']
get_visible_routes = config_vars['GetVisibleRoutes']
no_vehicle = config_vars['NoVehicle']

infopoint = requests.get(f'{infopoint_url}/{get_visible_routes}')

# -- Valid API Response ----------------------------------------------->
if infopoint.status_code == 200:
    routes = infopoint.json()
    for route in routes:
        if route['RouteId'] > 50: continue  # Skip specialty routes

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