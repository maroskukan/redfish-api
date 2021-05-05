import requests

url="http://127.0.0.1:8000/redfish/v1/Systems/437XR1138R2"

subitems = '''
Manufacturer
Model
SerialNumber
PowerState
BiosVersion
Description
'''.split()

r = requests.get(url, 
                verify=False).json()

for subitem in subitems:
    print(subitem + ": " + r[subitem])