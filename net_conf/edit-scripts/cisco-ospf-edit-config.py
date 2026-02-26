from netconf_class import session, netconf

config_snippet = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
              <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
					<ospf>
						<process-id>
							<id>1</id>
							<network>
								<ip>1.1.1.0</ip>
								<wildcard>0.0.0.255</wildcard>
								<area>9999</area>
							</network>
                            <network>
								<ip>1.1.3.0</ip>
								<wildcard>0.0.0.255</wildcard>
								<area>9999</area>
							</network>
                            <network>
								<ip>1.1.4.0</ip>
								<wildcard>0.0.0.255</wildcard>
								<area>9999</area>
							</network>
							<passive-interface>
								<default>true</default>
							</passive-interface>
							<router-id>2.2.2.0</router-id>
						</process-id>
					</ospf>
				</router-ospf>
			</router>
		</native>
</config>
"""

session.edit_config(target="running", payload=config_snippet)
session.get_to_file("edit-ospf.xml")
