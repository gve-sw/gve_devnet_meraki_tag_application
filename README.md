# Meraki Custom Tags: AutoTag Query and Enhancement
A script which can automatically apply a custom tag(s) to a set of client devices in a Systems Manager network based on the auto-tags applied by Meraki when the device is onboarded. 
In this case, a custom tag is applied to any device that contains an autoTag that flags it as being an Apple device.That tag can then be used to shape policy
across a broader range of device profiles.  

## Contacts
* Andrew Dunsmoor (adunsmoo@cisco.com)

## Solution Components
* Meraki Dashboard
* Meraki Systems Manager

## Installation/Configuration
Install the project dependencies with "pip install -r requirements.txt"


A config.py file must also be generated and completed. The required variables are as follows:

```python
#environment.env
API_KEY = ""    # Meraki Dashboard API Key
ORG_ID = 'https://api.meraki.com/api/v1'  #Meraki Dashboard URL
NET_ID = '1234567'     # Meraki organization ID for your desired target org. 
```
If you don't know how to get your organization ID, follow these teps:
1. Log into the Meraki Dashboard (in the same browser)
2. Click on this URL: https://dashboard.meraki.com/api/v1/organizations
3. Find the organization you wish to configure and copy the ID. 

Methods to programmatically GET Organizations and Netowrk IDs have been included in the code comments. 

## Usage

Edit the python file for your desired autoTag matches and the tag you wish to implement. 

Run the script with "python3 apply_meraki_tags.py"

For continous application of the tag as new devices enter the network, the script can also be scheduled as a Cron Job or using a scheduler: https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily/

The script can also be triggered via webhook to respond to events in the network: https://developer.cisco.com/meraki/webhooks/


# Screenshots
In this case, we matched applied to SUPER_TAG to all Apple devices. 
Before running the script
![/IMAGES/0image.png](/IMAGES/before.png)
After running the script, we've tagged all Apple devices on the network.
![/IMAGES/0image.png](/IMAGES/after.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.