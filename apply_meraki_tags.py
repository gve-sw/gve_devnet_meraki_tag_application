"""
Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from dotenv import load_dotenv
import meraki
import os

load_dotenv('environment.env')

### MUST CREATE environment.env FILE WITH THE FOLLOWING VARIABLES ###
API_KEY = os.getenv('API_KEY')
network_id = os.getenv('NET_ID') # Optionally you can get this at runtime using the calls below

# Initialize Dashboard object
dashboard = meraki.DashboardAPI(API_KEY)


########################
# Uncomment if you need to get your org or network ID.
# Get organizations
# response = dashboard.organizations.getOrganizations()
# print(response)

# # Get networks
# response = dashboard.organizations.getOrganizationNetworks(
#     organization_id, total_pages='all'
# )
# print(response)
########################



#### Specify Tags and Targets Here ####

# Specify Target Strings to match
match_tag_list = ['ios', 'mac', 'apple'] # Here we match the apple/iOS Auto tags

# SPECIFY DESIRED NEW TAG TAG HERE
new_tag = 'SUPER_TAG'

# List the devices enrolled in an SM network with various specified fields and filters
# https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices
sm_devices_response = dashboard.sm.getNetworkSmDevices(
    network_id, total_pages='all', fields=['autoTags']
)

# print(sm_devices_response)

devices_without_tag =[]
device_names = []

# For all devices
# Check if the VPN tag is applied or not
# Then flag device if it matches the specified iderntifiers
for device in sm_devices_response:
    if new_tag not in device['tags']:
        for tag in device['autoTags']:
            for mac_identifier in match_tag_list:
                if mac_identifier.lower() in tag.lower():
                    devices_without_tag.append(device['id'])
                    device_names.append(device['name'])

# Remove duplicates
devices_without_tag = list(set(devices_without_tag))
# Print Results
print('Checked ' + str(len(sm_devices_response)) +f' devices. Here are the IDs of Apple devices without the {new_tag} tag')
print(devices_without_tag)
print('Device Names:')
print(device_names)

# If flagged devices are found
# Add the tag to the flagged devices
# https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags
if devices_without_tag:
    update_tags_response = dashboard.sm.modifyNetworkSmDevicesTags(
        network_id, updateAction='add', ids=devices_without_tag, tags=[new_tag],
    )

    # Print updates devices
    print(f'Added {new_tag} to the following devices:')
    for device in update_tags_response:
        print(device['id'])

print('Task Complete')

# Included is an API call to remove the flag if desired.
remove_tag = dashboard.sm.modifyNetworkSmDevicesTags(
    network_id, scope=['withAny', new_tag], updateAction='delete', tags=[new_tag],
)
