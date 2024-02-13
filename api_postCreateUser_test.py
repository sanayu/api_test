import requests
# import json


def get_post_create_user():
	url = "https://reqres.in/api/users"
	myobj = {"name": "morpheus","job": "leader"}
	response = requests.post(url, json = myobj)
	assert response.status_code==201
	print(response.status_code)