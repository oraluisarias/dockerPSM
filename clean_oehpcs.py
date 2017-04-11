#!/bin/python
##create event hub cloud
##Mantainer: Topiltzin Flores
import json, sys, DC, PSM_Docker
	
IDENTITY_DOMAIN=sys.argv[1]

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
services_json = psm_client.run( ["psm", "oehcs", "services"] )
services = json.loads( services_json )
for service in services['services']:
	print ("Deleting OEHCS... ", service)
	print ("psm oehcs delete-service -s",  service)
	psm_client.run( ["psm", "oehcs", "delete-service", "-s", service, "-f", "true"] )

services_json = psm_client.run( ["psm", "oehpcs", "services"] )
services = json.loads( services_json )
for service in services['services']:
	print ("Deleting OEHPCS... ", service)
	psm_client.run( ["psm", "oehpcs", "delete-service", "-s", service, "-f", "true"] )

