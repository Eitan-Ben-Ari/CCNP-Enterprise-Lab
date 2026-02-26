from netconf_class import netconf, session
from pprint import pprint
filter="""
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<ip>
<access-list>
<extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
</extended>
</access-list>
</ip>
</native>
"""
session.get_config(filter_string=filter)
session.get_to_file(file_name="cisco-ios-xe-acl.xml")
mydict = session.json_object(file_name="dict")
pprint(mydict["rpc-reply"]["data"]["native"]["ip"]["access-list"])