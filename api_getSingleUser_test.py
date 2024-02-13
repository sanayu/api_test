import requests
# import json

def get_single_user():
	url = 'https://reqres.in/api/'
	user = 'users/2'
	response = requests.get(url+user)
	assert response.status_code == 200
	print(response)