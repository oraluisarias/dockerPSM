#!/bin/python
##clean container cloud
##Mantainer: Luis Arias
import docker, json
	
client = docker.DockerClient(base_url='tcp://hq-techadmin.us.oracle.com:2375')
path="psm_container"

USERNAME="cloud.admin"
PASSWORD="WorMy@2CYcle"
IDENTITY_DOMAIN="gse00010205"
DATACENTER="europe"
DATACENTERPSM="emea"
# DATACENTERPSM=DATACENTER

tag="psm_"+IDENTITY_DOMAIN
buildargs={
		"USERNAME":USERNAME,
		"PASSWORD":PASSWORD,
		"IDENTITY_DOMAIN":IDENTITY_DOMAIN,
		"DATACENTER":DATACENTER,
		"DATACENTERPSM":DATACENTERPSM
}
# try:
# 	print (client.images.get(tag))
# except:
# 	print ("Image doesnt exist, Creating...")
client.images.build(path=path, tag=tag, buildargs=buildargs )

print (client.containers.run(tag, ["psm", "bdcsce", "services"]))