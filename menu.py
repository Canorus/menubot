import json
import os
from random import randint
import requests

b = os.path.dirname(os.path.abspath(__file__)) + '/'
with open(b + 'data.json') as f:
    d = json.load(f)

def cat(fl):
    kw = list()
    with open(b+'data.json') as f:
        j = json.load(f)
    food_category = list(j['data'].keys())
    for fi in fl:
        if fi in food_category:
            kw.append(fi)
    return kw

def local(kw):
    u = 'https://dapi.kakao.com/v2/local/search/keyword.json?category_group_code=FD6'
    with open(b+'kakao.json') as f:
        header = json.load(f)
    r = requests.get(u+'&query='+kw, headers=header)
    rj = r.json()
    res = list()
    for i in rj['documents']:
        res.append(i)
    n = randint(0,len(res)-1)
    res = res[n]
    m = '이름: '+res['place_name']+'\n주소: '+res['road_address_name']+'\n분류: '+res['category_name']+'\nTel: '+res['phone']+'\n\n'+res['place_url']
    return m

def pick(k):
    cat_ca = list()
    for ki in k:
        cat_ca.append(d['data'][ki][randint(0,len(d['data'][ki])-1)])
    if len(cat_ca) < 1:
        can = list()
        for f in list(d['data'].keys()):
            for m in d['data'][f]:
                can.append(m)
        cat_ca.append(can[randint(0, len(can) - 1)])
        return cat_ca[0]
    else:
        r = cat_ca[randint(0, len(cat_ca) - 1)]
        return r
