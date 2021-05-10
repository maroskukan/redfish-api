from prettytable import PrettyTable
from requests import request
import sys


def SystemCollector(url, filter):
    # Retrieve Systems collection url
    base_path = url + '/redfish/v1'
    # Retrieve Systems collection url
    systems_path = request("GET",base_path, verify=False).json()['Systems']['@odata.id']
    # Retrieve Members from System collection
    system_members = request("GET", url+systems_path, verify=False).json()['Members']
    collection = []
    for system_member in system_members:
        system_member_path = system_member['@odata.id']
        subitems = request("GET", url+system_member_path, verify=False).json()

        member = {}
        for item in filter:
            member[str(item)] = subitems[item]
        collection.append(member)
    return collection


def TablePrinter(collection):
    pt_header = list(collection[0].keys())
    pt = PrettyTable(pt_header)
    pt.align = "l"
    for member in collection:
        row = list(member.values())
        pt.add_row(row)
    print(pt)
    return None
        

def main():
    url = 'http://localhost:8000'
    filter = '''
    Id
    HostName
    AssetTag
    SerialNumber
    Description
    PowerState
    '''.split()

    collection = SystemCollector(url, filter) 
    TablePrinter(collection)


if __name__ == '__main__':
    main()