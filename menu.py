import json
import os
from random import randint

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