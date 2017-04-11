#!/bin/python
##create container cloud
##Mantainer: Topiltzin Flores
import json, sys, DC, PSM_Docker
	
IDENTITY_DOMAIN="gse00003045"

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
services_json = psm_client.run( ["psm", "CONTAINER", "services"] )
services = json.loads( services_json )
print ( services )