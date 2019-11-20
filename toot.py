import requests
import os
import json
from credential import retrieve

base = os.path.dirname(os.path.abspath(__file__)) + '/'
instance = 'https://canor.kr'
try:
    # with open(base+'credential.json') as f:
    #     cred = json.load(f)
    # instance = cred['instance']
    # username = cred['credential']['id']['username']
    # acc = cred['credential']['id']['acc']
    acc = retrieve('menubot',instance)
    status_h = {'Authorization':'Bearer '+acc}
except:
    print('no credential found')
    raise ValueError

def sendtoot(s, cb=None, to=None):
    da = dict()
    da['status'] = s
    da['spoiler_text']='오늘 메뉴는'
    da['visibility'] = 'unlisted'
    if to:
        da['in_reply_to_id'] = to
    if cb:
        pass
    r = requests.post(instance + '/api/v1/statuses', headers=status_h, data=da)
    return r.json()['id']
