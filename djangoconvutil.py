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


def generic_hash(lst):
    lsthash = []
    for elem in lst:
        lsthash.append(elem)
    hashinputcand = "|".join(lsthash)
    m = hashlib.md5()
    m.update(hashinputcand)
    hashcand = m.hexdigest()
    return hashcand

def family_hash(lst):
    return generic_hash(lst) 

def caregiver_hash(lst):
    return generic_hash(lst) 

class CareGiver:
        Mum, Dad = range(2)

def write_preamble(f, gname):

    o1 = '''    members_organisation_1.name = u'{groupname}' '''

    f.write('''    from members.models import Organisation ''')
    f.write('\n')
    f.write('''    members_organisation_1 = Organisation() ''')
    f.write('\n')
    f.write(o1.format(groupname=gname))
    f.write('\n')
    f.write('''    members_organisation_1 = importer.save_or_locate(members_organisation_1) ''')
    f.write('\n')
    f.write('\n')

def write_caregivers(f, d, theidx, orgidx, familyidx, caregivertype):
    c1='''    members_caregiver_{idx} = Caregiver()'''
    c2='''    members_caregiver_{idx}.name_given = u'{firstname}' '''
    c3='''    members_caregiver_{idx}.name_family = u'{lastname}' '''
    c4='''    members_caregiver_{idx}.family = members_family_{family_idx} '''
    c5='''    members_caregiver_{idx}.phone_mobile = u'{mobile}' '''
    c6='''    members_caregiver_{idx}.email = u'{email}' '''
    c7='''    members_caregiver_{idx}.relationship = u'{reltype}' '''
    c8='''    members_caregiver_{idx} = importer.save_or_locate(members_caregiver_{idx}) '''

    if caregivertype == CareGiver.Mum:
        fname = d['Mum']
        mob = d['Mobile (mum)']
        rt = "MO"
    elif caregivertype == CareGiver.Dad:
        fname = d['Dad']
        mob = d['Mobile (dad)']
        rt = "FA"
    else:
        raise Exception("Undefined caregivertype")


    f.write(c1.format(idx=theidx))
    f.write('\n')
    f.write(c2.format(idx=theidx, firstname=fname)) 
    f.write('\n')
    f.write(c3.format(idx=theidx, lastname=d['Last name'])) 
    f.write('\n')
    f.write(c4.format(idx=theidx, family_idx=familyidx)) 
    f.write('\n')
    f.write(c5.format(idx=theidx, mobile=mob)) 
    f.write('\n')
    f.write(c6.format(idx=theidx, email=d['e-Mail'])) 
    f.write('\n')
    f.write(c7.format(idx=theidx, reltype=rt)) 
    f.write('\n')
    f.write(c8.format(idx=theidx)) 
    f.write('\n')
    f.write("") 
    f.write('\n')
    f.write('\n')

def write_family(f, d, theidx, cityname):

    f1='''    members_family_{idx} = Family()'''
    f1a='''    members_family_2.organisation = members_organisation_1 '''
    f2='''    members_family_{idx}.street_address = u'{sa}' '''
    f3='''    members_family_{idx}.suburb = u'{suburb}' '''
    f4='''    members_family_{idx}.city = u'{city}' '''
    f5='''    members_family_{idx}.phone_fixed = u'{phone}' '''
    f6='''    members_family_{idx} = importer.save_or_locate(members_family_{idx}) '''

    f.write(f1.format(idx=theidx))
    f.write('\n')
    f.write(f2.format(idx=theidx, sa=d['Street'])) 
    f.write('\n')
    f.write(f3.format(idx=theidx, suburb=d['Suburb'])) 
    f.write('\n')
    f.write(f4.format(idx=theidx, city=cityname)) 
    f.write('\n')
    f.write(f5.format(idx=theidx, phone=d['Phone'])) 
    f.write('\n')
    f.write(f6.format(idx=theidx)) 
    f.write('\n')
    f.write("") 
    f.write('\n')
    f.write('\n')

