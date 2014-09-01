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

def family_hash(d):
    fam_hsh = generic_hash([d['Street'].strip().lower()])
    return fam_hsh

def caregiver_hash_mum(d):
    cg_mum_hsh = generic_hash([d['Mum'].strip().lower(), d['Last name'].strip().lower(), d['Street'].strip().lower()])
    return cg_mum_hsh
def caregiver_hash_dad(d):
    cg_dad_hsh = generic_hash([d['Dad'].strip().lower(), d['Last name'].strip().lower(), d['Street'].strip().lower()])
    return cg_dad_hsh

def find_family_idx_from_hash(d, famdic):
    fam_hsh = family_hash(d)
    return famdic[fam_hsh]

def find_primary_caregiver_idx_from_hash(d, cgdic):
    cg_mum_hsh = caregiver_hash_mum(d)
    cg_dad_hsh = caregiver_hash_dad(d)

    outidx = None
    if cg_mum_hsh in cgdic:
        outidx = cgdic[cg_mum_hsh]
    elif cg_dad_hsh in cgdic:
        outidx = cgdic[cg_dad_hsh]
    else:
        outidx = None

    return outidx
    

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

    f.write('''    fees_year_1 = Year() ''')
    f.write('\n')
    f.write('''    fees_year_1.organisation = members_organisation_1 ''')
    f.write('\n')
    f.write('''    fees_year_1.name = u'Calendar 2013' ''')
    f.write('\n')
    f.write('''    fees_year_1.start = dateutil.parser.parse("2013-01-01") ''')
    f.write('\n')
    f.write('''    fees_year_1.end = dateutil.parser.parse("2013-12-31") ''')
    f.write('\n')
    f.write('''    fees_year_1 = importer.save_or_locate(fees_year_1) ''')
    f.write('\n')
    f.write('''    fees_year_2 = Year() ''')
    f.write('\n')
    f.write('''    fees_year_2.organisation = members_organisation_1 ''')
    f.write('\n')
    f.write('''    fees_year_2.name = u'Calendar 2014' ''')
    f.write('\n')
    f.write('''    fees_year_2.start = dateutil.parser.parse("2014-01-01") ''')
    f.write('\n')
    f.write('''    fees_year_2.end = dateutil.parser.parse("2014-12-31") ''')
    f.write('\n')
    f.write('''    fees_year_2 = importer.save_or_locate(fees_year_2) ''')
    f.write('\n')
    f.write('''    fees_year_3 = Year() ''')
    f.write('\n')
    f.write('''    fees_year_3.organisation = members_organisation_1 ''')
    f.write('\n')
    f.write('''    fees_year_3.name = u'Calendar 2015' ''')
    f.write('\n')
    f.write('''    fees_year_3.start = dateutil.parser.parse("2015-01-01") ''')
    f.write('\n')
    f.write('''    fees_year_3.end = dateutil.parser.parse("2015-12-31") ''')
    f.write('\n')
    f.write('''    fees_year_3 = importer.save_or_locate(fees_year_3) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_13_1 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_13_1.year = fees_year_1 ''')
    f.write('\n')
    f.write('''    fees_subyear_13_1.name = u'Term 1' ''')
    f.write('\n')
    f.write('''    fees_subyear_13_1.start = dateutil.parser.parse("2013-01-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_1.end = dateutil.parser.parse("2013-03-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_1 = importer.save_or_locate(fees_subyear_13_1) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_13_2 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_13_2.year = fees_year_1 ''')
    f.write('\n')
    f.write('''    fees_subyear_13_2.name = u'Term 2' ''')
    f.write('\n')
    f.write('''    fees_subyear_13_2.start = dateutil.parser.parse("2013-04-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_2.end = dateutil.parser.parse("2013-06-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_2 = importer.save_or_locate(fees_subyear_13_2) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_13_3 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_13_3.year = fees_year_1 ''')
    f.write('\n')
    f.write('''    fees_subyear_13_3.name = u'Term 3' ''')
    f.write('\n')
    f.write('''    fees_subyear_13_3.start = dateutil.parser.parse("2013-07-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_3.end = dateutil.parser.parse("2013-09-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_3 = importer.save_or_locate(fees_subyear_13_3) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_13_4 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_13_4.year = fees_year_1 ''')
    f.write('\n')
    f.write('''    fees_subyear_13_4.name = u'Term 4' ''')
    f.write('\n')
    f.write('''    fees_subyear_13_4.start = dateutil.parser.parse("2013-08-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_4.end = dateutil.parser.parse("2013-12-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_13_4 = importer.save_or_locate(fees_subyear_13_4) ''')
    f.write('\n')
    f.write('\n')


    f.write('''    fees_subyear_14_1 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_14_1.year = fees_year_2 ''')
    f.write('\n')
    f.write('''    fees_subyear_14_1.name = u'Term 1' ''')
    f.write('\n')
    f.write('''    fees_subyear_14_1.start = dateutil.parser.parse("2014-01-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_1.end = dateutil.parser.parse("2014-03-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_1 = importer.save_or_locate(fees_subyear_14_1) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_14_2 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_14_2.year = fees_year_2 ''')
    f.write('\n')
    f.write('''    fees_subyear_14_2.name = u'Term 2' ''')
    f.write('\n')
    f.write('''    fees_subyear_14_2.start = dateutil.parser.parse("2014-04-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_2.end = dateutil.parser.parse("2014-06-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_2 = importer.save_or_locate(fees_subyear_14_2) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_14_3 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_14_3.year = fees_year_2 ''')
    f.write('\n')
    f.write('''    fees_subyear_14_3.name = u'Term 3' ''')
    f.write('\n')
    f.write('''    fees_subyear_14_3.start = dateutil.parser.parse("2014-07-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_3.end = dateutil.parser.parse("2014-09-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_3 = importer.save_or_locate(fees_subyear_14_3) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_14_4 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_14_4.year = fees_year_2 ''')
    f.write('\n')
    f.write('''    fees_subyear_14_4.name = u'Term 4' ''')
    f.write('\n')
    f.write('''    fees_subyear_14_4.start = dateutil.parser.parse("2014-08-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_4.end = dateutil.parser.parse("2014-12-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_14_4 = importer.save_or_locate(fees_subyear_14_4) ''')
    f.write('\n')
    f.write('\n')



    f.write('''    fees_subyear_15_1 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_15_1.year = fees_year_3 ''')
    f.write('\n')
    f.write('''    fees_subyear_15_1.name = u'Term 1' ''')
    f.write('\n')
    f.write('''    fees_subyear_15_1.start = dateutil.parser.parse("2015-01-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_1.end = dateutil.parser.parse("2015-03-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_1 = importer.save_or_locate(fees_subyear_15_1) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_15_2 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_15_2.year = fees_year_3 ''')
    f.write('\n')
    f.write('''    fees_subyear_15_2.name = u'Term 2' ''')
    f.write('\n')
    f.write('''    fees_subyear_15_2.start = dateutil.parser.parse("2015-04-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_2.end = dateutil.parser.parse("2015-06-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_2 = importer.save_or_locate(fees_subyear_15_2) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_15_3 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_15_3.year = fees_year_3 ''')
    f.write('\n')
    f.write('''    fees_subyear_15_3.name = u'Term 3' ''')
    f.write('\n')
    f.write('''    fees_subyear_15_3.start = dateutil.parser.parse("2015-07-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_3.end = dateutil.parser.parse("2015-09-30") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_3 = importer.save_or_locate(fees_subyear_15_3) ''')
    f.write('\n')
    f.write('\n')

    f.write('''    fees_subyear_15_4 = SubYear() ''')
    f.write('\n')
    f.write('''    fees_subyear_15_4.year = fees_year_3 ''')
    f.write('\n')
    f.write('''    fees_subyear_15_4.name = u'Term 4' ''')
    f.write('\n')
    f.write('''    fees_subyear_15_4.start = dateutil.parser.parse("2015-08-01") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_4.end = dateutil.parser.parse("2015-12-31") ''')
    f.write('\n')
    f.write('''    fees_subyear_15_4 = importer.save_or_locate(fees_subyear_15_4) ''')
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



def write_income_for(f, theidx, amount, memberidx, subyearlabel):
    i1 = '''    fees_income_{idx} = Income() '''
    i2 = '''    fees_income_{idx}.subyear = {syl} '''
    i3 = '''    fees_income_{idx}.member = members_member_{memidx} '''
    i4 = '''    fees_income_{idx}.received = u'{amount}' '''
    i5 = '''    fees_income_{idx} = importer.save_or_locate(fees_income_{idx}) '''

    f.write(i1.format(idx=theidx))
    f.write('\n')
    f.write(i2.format(idx=theidx, syl=subyearlabel))
    f.write('\n')
    f.write(i3.format(idx=theidx, memidx=memberidx))
    f.write('\n')
    f.write(i4.format(idx=theidx, amount=amount))
    f.write('\n')
    f.write(i5.format(idx=theidx))
    f.write('\n')
    f.write('\n')

def write_income(f, d, theidx, memberidx):

    if d['2013 Term1'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2013 Term1'], memberidx, 'fees_subyear_13_1')
        theidx += 1

    if d['2013 Term 2'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2013 Term 2'], memberidx, 'fees_subyear_13_2')
        theidx += 1

    if d['2013 Term 3'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2013 Term 3'], memberidx, 'fees_subyear_13_3')
        theidx += 1

    if d['2013 Term 4'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2013 Term 4'], memberidx, 'fees_subyear_13_4')
        theidx += 1

    if d['2014 Term1'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2014 Term1'], memberidx, 'fees_subyear_14_1')
        theidx += 1

    if d['2014 Term 2'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2014 Term 2'], memberidx, 'fees_subyear_14_2')
        theidx += 1

    if d['2014 Term 3'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2014 Term 3'], memberidx, 'fees_subyear_14_3')
        theidx += 1

    if d['2014 Term 4'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2014 Term 4'], memberidx, 'fees_subyear_14_4')
        theidx += 1

    if d['2015 Term1'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2015 Term1'], memberidx, 'fees_subyear_15_1')
        theidx += 1

    if d['2015 Term 2'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2015 Term 2'], memberidx, 'fees_subyear_15_2')
        theidx += 1

    if d['2015 Term 3'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2015 Term 3'], memberidx, 'fees_subyear_15_3')
        theidx += 1

    if d['2015 Term 4'] == "":
        pass
    else:
        write_income_for(f, theidx, d['2015 Term 4'], memberidx, 'fees_subyear_15_4')
        theidx += 1

    return theidx



def write_member(f, d, theidx, familyidx, primarycgidx):

    #m5='''    members_member_{idx}.sub_organistion = sub_organisation_{idx} '''

    m1='''    members_member_{idx} = Member() '''
    m2='''    members_member_{idx}.name_given = u'{namegiven}' '''
    m3='''    members_member_{idx}.name_family = u'{namefamily}' '''
    m4='''    members_member_{idx}.organisation = members_organisation_1 '''
    m5='''    members_member_{idx}.sub_organistion = None '''
    m6='''    members_member_{idx}.membership_type = u'{memtype}' '''
    m7='''    members_member_{idx}.family = members_family_{famidx} '''
    m8='''    members_member_{idx}.primary_caregiver = members_caregiver_{primarycgidx} '''
    m9='''    members_member_{idx}.date_of_birth = dateutil.parser.parse('{dob}') '''
    m10='''    members_member_{idx}.date_invested = dateutil.parser.parse('{dinv}') '''
    m11='''    members_member_{idx} = importer.save_or_locate(members_member_1) '''

    if d['Member'] == 'Venturer':
        membertype = 'VE'
    elif d['Member'] == 'Scout':
        membertype = 'SC'
    elif d['Member'] == 'Cub':
        membertype = 'CU'
    elif d['Member'] == 'Kea':
        membertype = 'KE'
    else:
        raise Exception("Undefined membertype")

    if d['D.O.B'] == "":
        dob = None
    else:
        dob = None
        lstdob = d['D.O.B'].split('/')
        dob = lstdob[2] + '-' + lstdob[1] + '-' +  lstdob[0]

    if d['Invested'] == "":
        dinv = None
    else:
        #Hideous kludge to deal with one row
        if d['Invested'] == "Nov-05":
            lstinv = ["1","11","05"] 
        else:
            lstinv = d['Invested'].split('/')

        dinv = None
        lstinv = d['Invested'].split('/')
        try:
            dinv = lstinv[2] + '-' + lstinv[1] + '-' +  lstinv[0]
        except:
            print "!!!!!! "
            print lstinv
            print "!!!!!! "


    f.write(m1.format(idx=theidx))
    f.write('\n')
    f.write(m2.format(idx=theidx, namegiven=d['First name'])) 
    f.write('\n')
    f.write(m3.format(idx=theidx, namefamily=d['Last name'])) 
    f.write('\n')
    f.write(m4.format(idx=theidx)) 
    f.write('\n')
    f.write(m5.format(idx=theidx)) 
    f.write('\n')
    f.write(m6.format(idx=theidx, memtype=membertype)) 
    f.write('\n')
    f.write(m7.format(idx=theidx, famidx=familyidx)) 
    f.write('\n')
    if primarycgidx:
        f.write(m8.format(idx=theidx, primarycgidx=primarycgidx)) 
        f.write('\n')
    if dob:
        f.write(m9.format(idx=theidx, dob=dob)) 
        f.write('\n')
    if dinv:
        f.write(m10.format(idx=theidx, dinv=dinv)) 
        f.write('\n')
    f.write(m11.format(idx=theidx)) 
    f.write('\n')
    f.write('\n')

