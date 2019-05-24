import requests

resp = requests.get("https://api.github.com/users/gmak64/repos")
if resp.status_code != 200:
    raise ApiError('GET /users/gmak64/repos {}'.format(resp.status_code))
for item in resp.json():
    print(item['full_name'])
