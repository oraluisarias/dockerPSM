#!/bin/python
##create container cloud
##Mantainer: Topiltzin Flores
import json, sys, DC, PSM_Docker,time
	
IDENTITY_DOMAIN=sys.argv[1]

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
print ("Start the Clean process on Identity domain: ", IDENTITY_DOMAIN)
services_json = psm_client.run( ["psm", "bdcsce", "services"] )
print("Output of the psm command", services_json)
lines = services_json.replace("\n\x1b[1mWARNING\x1b[0m: A new version of psm client is available. Please run \'psm update\' to update to the latest version.\n","")

print ("without warnign ", lines)
services = json.loads( lines )
print("This is the list of services to be deleted: ", services)
for service in services['services']:
	print ("Deleting... ", service)
	psm_client.run( ["psm", "bdcsce", "delete-service", "-s", service, "-f", "true"] )
	print("Wait 7 min until the delete process finish......")
	time.sleep(420)
print("Finish the Clean process......")

