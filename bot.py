import menu
import toot
from credential import retrieve
import requests
import json
from bs4 import BeautifulSoup as bs

instance = 'https://canor.kr'
acc = retrieve('menubot', instance)
status_h = {'Authorization':'Bearer '+acc}

uri_user = instance + '/api/v1/streaming/user'
r_user = requests.get(uri_user, headers=status_h, stream=True)
print('Timeline connected')

for l in r_user.iter_lines():
    dec = l.decode('utf-8')
    if dec == 'event: notification':
        mode = 1
    elif dec == 'event: update':
        mode = 0
    elif dec == ':thump':
        mode = 0
    if mode:  # event: notification
        try:
            newdec = json.loads(dec.replace('data: ', ''))
            #print(newdec)
            if newdec['account']['bot']:
                raise
            try:
                t = newdec['type']
            except:
                pass
            if t == 'mention':
                reply_to_id = newdec['status']['id']
                reply_to_account = newdec['account']['acct']
                in_text = bs(newdec['status']['content'],'html.parser').get_text()
                print(in_text)
                in_status = in_text.split(' ')
                print(in_status)
                if '지역' in in_status:
                    status = menu.local(in_text.split('지역')[-1]) + '\n\n @'+reply_to_account
                else:
                    m = menu.cat(in_status)
                    p = menu.pick(m)
                    status = '추천 메뉴는 ' + p + '!!! \n@'+reply_to_account
                print(status)
                r = toot.sendtoot(status, to=reply_to_id)
                print(r)
            elif t == 'follow':
                new_follow = newdec['account']['id']
                print('new follower: ' + new_follow)
                t = requests.post(instance + '/api/v1/accounts/' + new_follow + '/follow', headers=status_h)
                print(t.content.decode('utf-8'))
        except:
            print('error occurred')
            pass
