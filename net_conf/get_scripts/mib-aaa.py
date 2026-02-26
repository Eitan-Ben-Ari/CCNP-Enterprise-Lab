from netconf_class import netconf, session

filter="""

<yang-library xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-library"/>
"""
session.get(filter_string=filter)
session.get_to_file("ietf-yang-library.xml")