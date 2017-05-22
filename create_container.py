#!/bin/python
##create container cloud
##Mantainer: Luis Arias
import requests, json, os, time, sys, subprocess, DC, PSM_Docker 

root_dir = os.path.dirname(os.path.realpath(__file__))	
IDENTITY_DOMAIN=sys.argv[1]


psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)

DATACENTER = psm_client.getDataCenterShort()

#services_json = psm_client.run( ["psm", "CONTAINER", "services"] )
#services = json.loads( services_json )
#print ( psm_client.run( ["psm", "log"] ) )

f=open(root_dir + "/templates/container_default_image.json")
container_image = f.read()
f.close()
container_image=container_image.replace('"','\"')
container_image=container_image.rstrip()

print container_image 
print ("Creating CONTAINER  service with PSM on:", IDENTITY_DOMAIN)

print (psm_client.run(['/usr/bin/bash','-c',"echo '" +container_image + "' > container_image.json && psm CONTAINER create-service -c container_image.json" ] ))
