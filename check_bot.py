import requests
import time
from datetime import datetime
import key_value

token = key_value.token
version_api = key_value.version_api
url = key_value.url


def time_obj(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")


def get_time(id):
    # get now time
    time_now = datetime.now().strftime("%Y-%m-%d")
    time_create = ''
    res = str(requests.get('https://vk.com/foaf.php?id=' + str(id))._content).split()
    for i in res:
        if i == '<ya:created':
            # get time create page
            time_create = res[res.index(i) + 1][9:19]
            break
    return (time_obj(time_now) - time_obj(time_create)).days


#print(get_time(562258816))
# def GetInfoUser(id):
# user = []
# response = requests.get(url + 'users.get', params={}
