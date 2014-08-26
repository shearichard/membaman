from data.djangoconvdata import lstHeaders
from data.djangoconvdata import lstDics

import hashlib
lstDicsHashed = []
for d in lstDics:
    dout = d
    lsthash = []
    lsthash.append(d['D.O.B'])
    lsthash.append(d['First name'])
    lsthash.append(d['Last name'])
    hashinputcand = "|".join(lsthash)
    m = hashlib.md5()
    m.update(hashinputcand)
    hashcand = m.hexdigest()
    dout['hash'] = hashcand
    lstDicsHashed.append(dout)

keylist = []
hashlist = []
unique_em = {}
unique_mobm = {}
unique_mobd = {}
for d in lstDicsHashed:
    if d['e-Mail'] == "":
        print "X" + " " + d['hash']
    lsthash = []
    lsthash.append(d['D.O.B'])
    lsthash.append(d['First name'])
    lsthash.append(d['Last name'])
    hashinputcand = "|".join(lsthash)
    m = hashlib.md5()
    m.update(hashinputcand)
    hashcand = m.hexdigest()
    if hashcand in hashlist:
        print "Y"
    else:
        hashlist.append(hashcand)

    if d['e-Mail'] in unique_em:
        unique_em[d['e-Mail']] += 1
    else:
        unique_em[d['e-Mail']] = 1

    for k in d.keys():
        if k in keylist:
            pass
        else:
            keylist.append(k)

'''
import pprint
keylist.sort()
pprint.pprint(keylist)
print hashlist
'''




