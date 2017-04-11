#!/usr/bin/env python
#################################################################################
#************************************************************************************************#
# Script: PSM_Docker.py                                                                          #
# Usage : GSE - PSM wrapper for docker 													         #
# Date                                  Who                           What                       #
#------------------------------------------------------------------------------------------------#
# Mar-2017                           LUISARIA.MX                  Initial Version                #
#------------------------------------------------------------------------------------------------#
import requests, json, os, time, sys, subprocess, DC, docker

class PSM_CLIENT:	
	def __init__(self, identity_domain):		
		self.root_dir = os.path.dirname(os.path.realpath(__file__))
		self.IDENTITY_DOMAIN=identity_domain
		self.DC_header_token = {
			'Authorization': 'Bearer YTg3ZWJmNDctNzFhYS00ZDM4LWE5YWQtN2FlNTNlZjNlNTNm'
		}
		self.DATACENTER_SHORT = self.findDataCenter()
		if self.DATACENTER_SHORT == "us2" :
			self.DATACENTER_LONG="us"
		elif self.DATACENTER_SHORT == "em2" :
			self.DATACENTER_LONG="emea"
		self.dc_environment = self.getDCEnvironment()
		self.buildContainer()

	def getDataCenterLong(self):
		return self.DATACENTER_LONG

	def getDataCenterShort(self):
		return self.DATACENTER_SHORT

	def getDCEnvironment(self):
		self.environment_name="metcs-"+self.IDENTITY_DOMAIN
		self.USERNAME="cloud.admin"
		self.PASSWORD=dc_environment["items"][0]["password"]		
		print ("Password: ", self.PASSWORD)
		return self.getDCEnvironment(self.environment_name)

	def buildContainer(self):		
		path=os.path.join(self.root_dir, "psm_container")
		self.tag="psm_"+self.IDENTITY_DOMAIN
		self.buildargs={
				"USERNAME":self.USERNAME,
				"PASSWORD":self.PASSWORD,
				"IDENTITY_DOMAIN":self.IDENTITY_DOMAIN,
				"DATACENTER":self.DATACENTER_LONG,
				"DATACENTERPSM":self.DATACENTER_LONG
		}
		self.client = docker.DockerClient(base_url='tcp://hq-techadmin.us.oracle.com:2375')
		try:
			self.client.images.remove( image=self.tag, force=True )
		except:
			print ("Image doesnt exist, Creating...")
		print ("Container source ", path)
		print (self.client.images.build(path=path, tag=self.tag, buildargs=self.buildargs ))
		print (self.client.images.get(self.tag))
		print ("Connected to docker daemon and using psm client version ", self.client.containers.run(self.tag, ["psm", "-v"]))		

	def run(self, cmds):
		return self.client.containers.run( self.tag, cmds )

	def getIdentityDomain(self):
		return self.IDENTITY_DOMAIN

	def getUsername(self):
		return self.USERNAME

	def getPassword(self):
		return self.PASSWORD

	def getClient(self):
		return self.client

	def findDataCenter(self):
		datacenters = ["us2", "em2"]
		DC_header_token = {
			'X-Auth-Token': 'AUTH_tk3cbd98e962069a0e22abc9e119962831'
		}
		for dc in datacenters:
			endpoint = "https://" + dc + ".storage.oraclecloud.com/v1/Storage-"+self.IDENTITY_DOMAIN+"/test"
			response =  requests.put(endpoint, headers = DC_header_token).text
			if response != "<html><body>Sorry, but the content requested does not seem to be available. Try again later. If you still see this message, then contact Oracle Support.</body></html>":
				return dc
		return False

	def saveDCEnvironmentPassword(self, environment_id, new_pass):		
		endpoint = "https://adsweb.oracleads.com/apex/adsweb/rest/environments/" + str(environment_id) + "/password"		
		pass_data = {
			"password" : new_pass
		}
		return requests.put(endpoint, data=json.dumps(pass_data), headers=self.DC_header_token )
		
	def getDCEnvironment(self):
		self.environment_name="metcs-"+self.IDENTITY_DOMAIN
		print ("Getting environment username/password from Demo Central...")
		endpoint = "https://adsweb.oracleads.com/apex/adsweb/rest/environments"
		headers = self.DC_header_token
		headers['X-Oracle-Environment-Name'] = self.environment_name
		dc_environment = json.loads( requests.get(endpoint, headers=headers).text )		
		self.USERNAME="cloud.admin"
		self.PASSWORD=dc_environment["items"][0]["password"]		
		print ("Password: ", self.PASSWORD)
		return dc_environment

	def saveDCSSHKey(self):
		public_key = open(os.path.join(self.root_dir, "psm/default_ssh_key/id_rsa.pub")).read()
		private_key = open(os.path.join(self.root_dir, "psm/default_ssh_key/id_rsa")).read()
		sshhey_payload = { 
			"service_name":"default", 
			"key_public":public_key, 
			"key_private":private_key, 
			"IDENTITY_DOMAIN":self.IDENTITY_DOMAIN, 
		} 
		requests.put(sshkeys_endpoint, data=json.dumps(sshkey_payload), header=self.DC_header_token)
		return public_key