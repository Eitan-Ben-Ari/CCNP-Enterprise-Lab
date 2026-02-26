from netconf_class import netconf, session

session.get()
session.get_to_file("netconf-state.xml")

