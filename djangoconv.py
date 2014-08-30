import hashlib

import tempfile
import os

from data.djangoconvdata import lstHeaders
from data.djangoconvdata import lstDics

from djangoconvutil import getTempPath 
from djangoconvutil import update_unique_counts
from djangoconvutil import cull_unique_counts
from djangoconvutil import family_hash
from djangoconvutil import write_caregiver
from djangoconvutil import write_family
 

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

    update_unique_counts(d, unique_em, 'e-Mail')
    update_unique_counts(d, unique_mobd, 'Mobile (dad)')
    update_unique_counts(d, unique_mobm, 'Mobile (mum)')

    for k in d.keys():
        if k in keylist:
            pass
        else:
            keylist.append(k)

import pprint
cull_unique_counts(unique_em, 1)
cull_unique_counts(unique_mobd, 1)
cull_unique_counts(unique_mobm, 1)
pprint.pprint(unique_em)
pprint.pprint(unique_mobd)
pprint.pprint(unique_mobm)

import pdb

famdic = {}
fam_out = getTempPath("famout")
with open(fam_out, 'w') as f:
    thefamilyidx = 1
    for d in lstDics:
        famhsh = family_hash([d['Street'].strip().lower()])
        if famhsh in famdic:
            print d['Street'] 
        else:
            famdic[famhsh] = None
            write_family(f, d, thefamilyidx)
            thefamilyidx += 1


    
print fam_out
