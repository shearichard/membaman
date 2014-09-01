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
from djangoconvutil import caregiver_hash_mum
from djangoconvutil import caregiver_hash_dad
from djangoconvutil import write_caregivers
from djangoconvutil import write_family
from djangoconvutil import write_preamble
from djangoconvutil import write_member
from djangoconvutil import write_income
from djangoconvutil import CareGiver 
from djangoconvutil import find_family_idx_from_hash
from djangoconvutil import find_primary_caregiver_idx_from_hash
 

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
memtype_dic ={}

for d in lstDicsHashed:
    if d['Member'] not in memtype_dic:
        memtype_dic[d['Member']] = None

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
    thememberidx = 1
    theincomeidx = 1
    for d in lstDics:
        #fam_hsh = family_hash([d['Street'].strip().lower()])
        fam_hsh = family_hash(d)
        cg_mum_hsh = caregiver_hash_mum(d)
        cg_dad_hsh = caregiver_hash_dad(d)
        if fam_hsh in famdic:
            print d['Street'] 
        else:
            famdic[fam_hsh] = thefamilyidx
            write_family(f, d, thefamilyidx, strCityName)
            primarycgidx = None
            if cg_mum_hsh in cgdic:
                print d['Mum']
            else:
                cgdic[cg_mum_hsh] = thecaregiveridx
                write_caregivers(f, d, thecaregiveridx, -1, find_family_idx_from_hash(d, famdic), CareGiver.Mum)
                thecaregiveridx += 1
            if cg_mum_hsh in cgdic:
                print d['Dad']
            else:
                cgdic[cg_dad_hsh] = thecaregiveridx
                write_caregivers(f, d, thecaregiveridx, -1, find_family_idx_from_hash(d, famdic), CareGiver.Dad)
                thecaregiveridx += 1
            thefamilyidx += 1

        write_member(f, d, thememberidx, find_family_idx_from_hash(d, famdic), find_primary_caregiver_idx_from_hash(d, cgdic))
        theincomeidx = write_income(f, d, theincomeidx, thememberidx)
        thememberidx += 1



    
print fam_out
print memtype_dic
