#!/bin/python
##create container cloud
##Mantainer: Luis Arias
import json, sys, DC, PSM_Docker
	
IDENTITY_DOMAIN=sys.argv[1]

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
services_json = psm_client.run( ["psm", "CONTAINER", "services"] )
services = json.loads( services_json )
for service in services['services']:
	print ("Deleting... ", service)
	psm_client.run( ["psm", "CONTAINER", "delete-service", "-s", service, "-f", "true"] )