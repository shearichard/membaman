import hashlib

import tempfile
import os

from data.djangoconvdata import lstHeaders
from data.djangoconvdata import lstDics
from data.djangoconvdata import strGroupName 
from data.djangoconvdata import strCityName 

from djangoconvutil import getTempPath 
from djangoconvutil import update_unique_counts
from djangoconvutil import cull_unique_counts
from djangoconvutil import family_hash
from djangoconvutil import caregiver_hash
from djangoconvutil import write_caregivers
from djangoconvutil import write_family
from djangoconvutil import write_preamble
from djangoconvutil import CareGiver 
 

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
cgdic = {}
fam_out = getTempPath("famout")
with open(fam_out, 'w') as f:
    write_preamble(f, strGroupName)
    thefamilyidx = 1
    thecaregiveridx = 1
    for d in lstDics:
        fam_hsh = family_hash([d['Street'].strip().lower()])
        cg_mum_hsh = caregiver_hash([d['Mum'].strip().lower(), d['Last name'].strip().lower(), d['Street'].strip().lower()])
        cg_dad_hsh = caregiver_hash([d['Dad'].strip().lower(), d['Last name'].strip().lower(), d['Street'].strip().lower()])
        if fam_hsh in famdic:
            print d['Street'] 
        else:
            famdic[fam_hsh] = None
            write_family(f, d, thefamilyidx, strCityName)
            if cg_mum_hsh in cgdic:
                print d['Mum']
            else:
                write_caregivers(f, d, thecaregiveridx, -1, thefamilyidx, CareGiver.Mum)
                thecaregiveridx += 1
            if cg_mum_hsh in cgdic:
                print d['Dad']
            else:
                write_caregivers(f, d, thecaregiveridx, -1, thefamilyidx, CareGiver.Dad)
                thecaregiveridx += 1
            thefamilyidx += 1


    
print fam_out
