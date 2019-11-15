import time

import requests

# Получить список всех пользователей данного сообщества
token = '7422c7857422c7857422c7854f744fe3a4774227422c78529b202d84e8e5d7223c5e291'
version_api = 5.101
group_id = 'fishinghd'
sort = 'id_asc'
url = 'https://api.vk.com/method/groups.getMembers'
fields = ['sex', 'bdate']
offset = 1000
all_users = []
users = []
while offset < 2000:
    response = requests.get(url,
                            params={'access_token': token,
                                    'v': version_api,
                                    'group_id': group_id,
                                    'sort': sort,
                                    'count': 1000,
                                    'fields': fields,
                                    'offset': offset})
    data = response.json()['response']['items']
    offset += 1000
    all_users.extend(data)
    time.sleep(0.3)
for user in all_users:
    if user['first_name'] == 'Alex':
        users.append(user['id'])
print(1)