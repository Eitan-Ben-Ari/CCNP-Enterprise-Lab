# NETCONF helper script for CCNP automation
# Author: Eitan
# Date: 2025-09-26

from ncclient import manager
from xml.dom import minidom
import xmltodict
import json

dfilt = '<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>'
dfilt2="""
<netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
</netconf-state>
"""

class netconf:
    def __init__(self, host: str, username: str, password: str): 
        self.host = host
        self.username = username
        self.password = password
        self.port=830
    def get_config(self, type="subtree", filter_string=dfilt): 
       with manager.connect(  # type: ignore
            host=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            hostkey_verify=False) as connection: 
                self.xml = connection.get_config(source="running", filter=(type, filter_string)).xml
    def edit_config(self, target, payload): 
       with manager.connect(  
            host=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            hostkey_verify=False) as connection: 
                self.xml = connection.edit_config(target=target, config=payload).xml
    def get(self, type="subtree", filter_string=dfilt2): 
       with manager.connect(  # type: ignore
            host=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            hostkey_verify=False) as connection: 
                
                self.xml = connection.get(filter=(type, filter_string)).xml
    
    def get_to_screen(self):
         print(minidom.parseString(self.xml).toprettyxml())
    def json_object(self, file_name=None):
         dic = xmltodict.parse(self.xml)
         if file_name:
             path = f"Get_responses/objects/{file_name}.json"
             with open(path, "w") as f:
                 f.write("data = ")
                 f.write(json.dumps(dic, indent=2))
             print(f"✔ Saved formatted object at {path}")
         return dic
          
    def get_to_file(self, file_name=None):
         if file_name == None:
              file_name= "%s.xml"  % self.host
         path= f'Get_responses/{file_name}'
         print(self.host)
         with open(path, 'w') as file:
                 file.write(minidom.parseString(self.xml).toprettyxml())
              

session = netconf('192.168.3.130', 'admin', '1234')

