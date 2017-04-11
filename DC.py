#!/usr/bin/env python
#################################################################################
#************************************************************************************************#
# Script: DC.py                                                                                 #
# Usage : GSE - Python wrapper to execute REST calls on Demo Central            #
# Date                                  Who                           What                       #
#------------------------------------------------------------------------------------------------#
# Aug-2016                           LUISARIA.MX                  Initial Version                #
#------------------------------------------------------------------------------------------------#
import requests, json, os, time, sys, subprocess

class DemoCentral:	
	def saveDCEnvironmentPassword(self, environment_id, new_pass):		
		endpoint = "https://adsweb.oracleads.com/apex/adsweb/rest/environments/" + str(environment_id) + "/password"
		headers = {
			'Authorization': 'Bearer YTg3ZWJmNDctNzFhYS00ZDM4LWE5YWQtN2FlNTNlZjNlNTNm'
		}
		pass_data = {
			"password" : new_pass
		}
		return requests.put(endpoint, data=json.dumps(pass_data), headers=headers )
		
	def getDCEnvironment(self, environment):
		print ("Getting environment username/password from Demo Central...")
		endpoint = "https://adsweb.oracleads.com/apex/adsweb/rest/environments"
		headers = {
			'Authorization': 'Bearer YTg3ZWJmNDctNzFhYS00ZDM4LWE5YWQtN2FlNTNlZjNlNTNm',
			'X-Oracle-Environment-Name': environment
		}
		return json.loads( requests.get(endpoint, headers=headers).text )		