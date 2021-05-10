from prettytable import PrettyTable
from requests import request
import sys


def SystemCollector(url, filter):
    """Gets URL of Redfish compatible system and keys defined as filter list.
    Returns a collection of systems with keys and their values.

    Args:
        url (str): Redfish Universal Resource Locator. Can contain FQDN or IP address with
        or without port information. For example 'http://localhost:8000'
        filter (list): List containing items that define individual keys that will be retrieved
        from system tree. For example ['Id', 'HostName', 'SerialNumber']
    
    Returns:
        collection (list): Each item in list contains dictionary that defines a system and its
        properties. For example. [{'Id': '437XR1138R2', 'HostName': 'web483', 'SerialNumber': '437XR1138R2'}]
    """
    # Create Redfish Base URL
    base_path = url + '/redfish/v1'
    # Retrieve Systems collection url
    systems_path = request("GET",base_path, verify=False).json()['Systems']['@odata.id']
    # Retrieve Members from System collection path
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
    
    # Example filter for public-rackmount1
    filter = '''
    Id
    HostName
    AssetTag
    SerialNumber
    Description
    PowerState
    '''.split()
    # # Example filter for public-bladed
    # filter = '''
    # Id
    # Manufacturer
    # '''.split()

    collection = SystemCollector(url, filter)

    TablePrinter(collection)


if __name__ == '__main__':
    main()