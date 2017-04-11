import requests, json, sys

headers = {
	"X-AUTH-TOKEN" : "Tr4nVHLBgJgXb52FMe5cQMJGkDT7AdqkbLzzxxh8LgYevcEXsSngrKkKKyy8VXPk", 
	"Content-Type" : "application/json", 
	"Accept" : "application/json"
}			
data = {"invitee_email":sys.argv[1],"account":"38","groups":sys.argv[2] }

endpoint = "https://oraclecloud.qubole.com/api/latest/users/invite_new"
endpoint2 = "https://oraclecloud.qubole.com/api/latest/account"
r = requests.post(endpoint, data=json.dumps(data), headers=headers)
# r = requests.get(endpoint2, data=json.dumps(data), headers=headers)
# print (r.text)
# data = {
# 	"_method":"put",
# 	"authenticity_token":"b2tem2PXzhsdU+hX62qQ3DfRVagVUlL+v7WGIg6jErY=",
# 	"confirmation_token":"mzzo7gKEsAHGBRED8EEh",
# 	"user":{
# 		"password":"welcome1",
# 		"password_confirmation":"welcome1"
# 	}
	
# }
# endpoint = "https://oraclecloud.qubole.com/user/confirmation"
# r = requests.post(endpoint, data=json.dumps(data))
# print (r.text)