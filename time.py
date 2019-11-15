# import requests
#
# owner_id = "506941436"
# token = '98f8d954ec5c80db364c563af23b43ca8db82e993a333e3ca98ae422d4c95795a050e99e2a62decd8b694'
# version = '5.103'
# r = requests.post(
#     'https://api.vk.com/method/execute?access_token=' + token + 'v' + version +
#     '&code=return API.wall.get({"owner_id":"' + owner_id + '","count":"1"});'
# )
# response_data = r.json()
# print(response_data)
import random
from datetime import datetime


def duplicate(data):
    arr = []
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            arr.append(data[i])
    return arr


array1, array2 = [], []
for i in range(1, 100000, 1):
    array1.append(i)
for i in range(94000, 193999, 1):
    array2.append(i)
random.shuffle(array1)
random.shuffle(array2)
start_time = datetime.now()
array1.extend(array2)
random.shuffle(array1)
duplicate(sorted(array1))
end_time = datetime.now()
print('Time optimisation: {}'.format(end_time - start_time))

'''arr = []
array3, array4 = [], []
for i in range(1, 100000, 1):
    array3.append(i)
for i in range(94000, 193999, 1):
    array4.append(i)
random.shuffle(array1)
random.shuffle(array2)
start_time = datetime.now()
for i in array3:
    for j in array4:
        if i == j:
            arr.append(i)
            break
end_time = datetime.now()
print('Time count: {}'.format(end_time - start_time))'''
