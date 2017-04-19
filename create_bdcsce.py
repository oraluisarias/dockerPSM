#!/bin/python
##Create BDCSCE Service PSM
##Mantainer: Topiltzin Flores
import requests, json, os, time, sys, subprocess, DC, PSM_Docker

root_dir = os.path.dirname(os.path.realpath(__file__))
IDENTITY_DOMAIN=sys.argv[1]

psm_client = PSM_Docker.PSM_CLIENT(IDENTITY_DOMAIN)
DATACENTER = psm_client.getDataCenterShort()
PASSWORD=psm_client.getPassword()
print("Template: ", root_dir ,"/templates/BDCSE_GSE.json")
print( "PATH: ", root_dir + '/templates/BDCSE_GSE.json')

f=open(root_dir + "/templates/BDCSE_GSE.json")
bigdata_image = f.read()
f.close()
USERNAME="cloud.admin"

print bigdata_image
print("LOG start")
print ("IDENTITY_DOMAIN: ",IDENTITY_DOMAIN)
print( "#DATACENTER: ", DATACENTER)
print( "#USERNAME: ", USERNAME)
print( "#PASSWORD: ", PASSWORD)
public_key = open(root_dir+ "/default_ssh_key/id_rsa.pub")
public_keyf=public_key.read().rstrip()
public_key.close()
bigdata_imagef=bigdata_image.replace( "#IDENTITY_DOMAIN", IDENTITY_DOMAIN)
bigdata_imagef=bigdata_imagef.replace( "#DATACENTER", DATACENTER)
bigdata_imagef=bigdata_imagef.replace( "#USERNAME", USERNAME)
bigdata_imagef=bigdata_imagef.replace( "#PASSWORD", PASSWORD)
bigdata_imagef=bigdata_imagef.replace( "#SSH_KEY", public_keyf)
bigdata_imagef=bigdata_imagef.replace('"','\"')
bigdata_imagef=bigdata_imagef.strip().rstrip().lstrip()

print bigdata_imagef
print ("Creating BDCSCE service with PSM on:", IDENTITY_DOMAIN)
big="TEST"
print (psm_client.run( ["psm", "bdcsce", "services"] ))
print("--- Create a file and do a cat")
##print(psm_client.run(["cat", "/etc/group"]))
print (psm_client.run(['/usr/bin/bash','-c',"echo '" + bigdata_imagef + "' > bigdata_image.json && cat bigdata_image.json"]))
##print (psm_client.run( [ 'sh ','-c',"echo '" + bigdata_imagef + "' > ~/bigdata_image.json   && psm bdcsce create-service -c ~/bigdata_image.json" ] ) )
print ("-----------------------------------------------------------------------------------------------END")
print (psm_client.run(['psm','bdcsce','create-service']))
print (psm_client.run(['/usr/bin/bash','-c',"echo '" + bigdata_imagef + "' > bigdata_image.json && psm bdcsce create-service -c bigdata_image.json" ] ))
##print (psm_client.run(['/usr/bin/bash','-c',"echo '" + bigdata_imagef + "' > bigdata_image.json && psm bdcsce services" ] ))

print ("Finish the creation of BDCSCE Cluster")


