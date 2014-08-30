import hashlib
import tempfile
import os

def makeTempDir():
    path2dir = tempfile.mkdtemp()
    return path2dir
def getTempPath(fName, dPath=None):
    if dPath==None:
        path2dir = makeTempDir()
    else:
        path2dir = dPath
    fullpath = os.path.join(path2dir,fName)
    return fullpath

def update_unique_counts(din, dcount,  k):
    '''
    Add an element keyed on `k` with a value
    of 1 or increment an element keyed on `k`
    by 1
    '''
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


def family_hash(lst):
    lsthash = []
    for elem in lst:
        lsthash.append(elem)
    hashinputcand = "|".join(lsthash)
    m = hashlib.md5()
    m.update(hashinputcand)
    hashcand = m.hexdigest()
    return hashcand

'''
    members_family_1 = Family()
    members_family_1.street_address = u'111 Acacia Avenue'
    members_family_1.suburb = u'Strathmore'
    members_family_1.city = u'Wellington'
    members_family_1.phone_fixed = u'04 555 1111'
    members_family_1 = importer.save_or_locate(members_family_1)
'''

'''

'''

def write_caregiver(f, d, theidx, familyidx):
    cm1='''    members_caregiver_{idx} = Caregiver()'''
    cm2='''    members_caregiver_{idx}.name_given = u'{firstname}' '''
    cm3='''    members_caregiver_{idx}.name_family = u'{lastname}' '''
    cm4='''    members_caregiver_{idx}.family = members_family_{family_idx} '''
    cm5='''    members_caregiver_{idx}.phone_mobile = u'{mobile}' '''
    cm6='''    members_caregiver_{idx}.email = u'{e-mail}' '''
    cm7='''    members_caregiver_{idx}.relationship = u'{reltype}' '''
    cm8='''    members_caregiver_{idx} = importer.save_or_locate(members_caregiver_{idx}) '''

    f.write(c1.format(idx=theidx))
    f.write('\n')
    f.write(c2.format(idx=theidx, sa=d['Street'])) 
    f.write('\n')
    f.write(c3.format(idx=theidx, suburb=d['Suburb'])) 
    f.write('\n')
    f.write(c4.format(idx=theidx)) 
    f.write('\n')
    f.write(c5.format(idx=theidx, phone=d['Phone'])) 
    f.write('\n')
    f.write(c6.format(idx=theidx)) 
    f.write('\n')
    f.write(c7.format(idx=theidx)) 
    f.write('\n')
    f.write(c8.format(idx=theidx)) 
    f.write('\n')
    f.write("") 
    f.write('\n')
    f.write('\n')

def write_family(f, d, theidx):

    f1='''    members_family_{idx} = Family()'''
    f2='''    members_family_{idx}.street_address = u'{sa}' '''
    f3='''    members_family_{idx}.suburb = u'{suburb}' '''
    f4='''    members_family_{idx}.city = u'Wellington' '''
    f5='''    members_family_{idx}.phone_fixed = u'{phone}' '''
    f6='''    members_family_{idx} = importer.save_or_locate(members_family_{idx}) '''

    f.write(f1.format(idx=theidx))
    f.write('\n')
    f.write(f2.format(idx=theidx, sa=d['Street'])) 
    f.write('\n')
    f.write(f3.format(idx=theidx, suburb=d['Suburb'])) 
    f.write('\n')
    f.write(f4.format(idx=theidx)) 
    f.write('\n')
    f.write(f5.format(idx=theidx, phone=d['Phone'])) 
    f.write('\n')
    f.write(f6.format(idx=theidx)) 
    f.write('\n')
    f.write("") 
    f.write('\n')
    f.write('\n')

