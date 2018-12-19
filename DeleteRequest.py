import requests

URL='https://reqres.in/api/users/2'
response=requests.delete(URL)
print(response)
print(response.status_code)
assert response.status_code==204
#test