from netconf_class import netconf, session


filter= """ 
<routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
 <control-plane-protocols>
 <control-plane-protocol>
 <type> 
 <ospf xmlns="urn:ietf:params:xml:ns:yang:ietf-ospf"/> 
 </type>
 </control-plane-protocol>
 </control-plane-protocols>
</routing>
"""
session.get_config(filter_string=filter)
session.get_to_screen()