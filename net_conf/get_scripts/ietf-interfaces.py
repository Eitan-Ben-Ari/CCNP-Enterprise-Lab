from netconf_class import netconf, session

session.get_config()
session.get_to_file("ietf-interfaces.xml")

