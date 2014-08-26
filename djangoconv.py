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

def update_unique_counts(din, dcount,  k):
    if din[k] in dcount:
        dcount[din[k]] += 1
    else:
        dcount[din[k]] = 1

def cull_unique_counts(dcount,  lowerlimit):
    '''
    Given a dictionary, dcount, for which each
    each element has an integer value remove
    all elements which are equal or lower than
    lowerlimit
    '''
    lst_keys_to_del = []
    for k in dcount:
        if dcount[k] <= lowerlimit:
            lst_keys_to_del.append(k)

    for k in lst_keys_to_del:
        del dcount[k]


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

    update_unique_counts(d, unique_em, 'e-Mail')
    update_unique_counts(d, unique_mobd, 'Mobile (dad)')
    update_unique_counts(d, unique_mobm, 'Mobile (mum)')

    for k in d.keys():
        if k in keylist:
            pass
        else:
            keylist.append(k)

def dupd(d, k):
    d[k] = d[k] ** 2

d = {'a':1, 'b':2, 'c':3}

print d
dupd(d, 'b')
print d

import pprint
cull_unique_counts(unique_em, 1)
cull_unique_counts(unique_mobd, 1)
cull_unique_counts(unique_mobm, 1)
pprint.pprint(unique_em)
pprint.pprint(unique_mobd)
pprint.pprint(unique_mobm)
'''
keylist.sort()
pprint.pprint(keylist)
print hashlist
'''




