#!/bin/python
##Create OEHPCS Service with PSM
##Mantainer: Topiltzin Flores
import json, sys, DC, PSM_Docker, os

root_dir = os.path.dirname(os.path.realpath(__file__))
IDENTITY_DOMAIN=sys.argv[1]

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
DATACENTER = psm_client.getDataCenterShort()

bigdata_image = open(os.path.join(root_dir, "psm/templates/OEHPCSCE_GSE.json")).read()
bigdata_image = replace(container_image, "#IDENTITY_DOMAIN", IDENTITY_DOMAIN)
bigdata_image = replace(container_image, "#DATACENTER", DATACENTER)
bigdata_image = replace(container_image, "#USERNAME", USERNAME)
bigdata_image = replace(container_image, "#PASSWORD", PASSWORD)
print("Creating OEHPCS service on:", IDENTITY_DOMAIN)
print ( psm_client.run( [ 'sh','-c',"echo '" + bigdata_image + "' > ~/bigdata_image.json && psm oehpcs create-service -c ~/bigdata_image.json" ] ) )	
