from django.db import models

class Organisation(models.Model):
    '''
    An `Organisation` is an entity to which 
    `Member` belong
    '''
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

class SubOrganisation(models.Model):
    '''
    A `SubOrganisation` is grouping within an 
    `Organisation` to which a `Member` primarily
    identifies 
    '''
    class Meta:
        ordering = ['sub_name']

    sub_name = models.CharField(max_length=50)
    organisation = models.ForeignKey(Organisation)

    def __unicode__(self):
        return unicode(self.sub_name) + unicode(' (') +  unicode(self.organisation.name) + unicode(')')

class Family(models.Model):
    '''
    `Family` constitutes one or more `Caregiver` and one or
    more `Member`
    '''
    class Meta:
        ordering = ['street_address', 'suburb','city']

    organisation = models.ForeignKey(Organisation)
    street_address = models.CharField(max_length=75)
    suburb = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone_fixed = models.CharField(max_length=20)

    def __unicode__(self):
        return u', '.join((unicode(self.street_address), unicode(self.suburb), unicode(self.city)))

class Person(models.Model):
    '''
    `Person` is an abstract Model to accomodate personal
    identity
    '''
    class Meta:
        abstract = True

    name_given = models.CharField('given name', max_length=50)
    name_family = models.CharField('family name', max_length=50)

class Caregiver(Person):
    '''
    `Caregiver` is someone who cares for a `Member`
    '''
    class Meta:
        ordering = ['name_given', 'name_family']

    MOTHER = 'MO'
    FATHER = 'FA'
    GRANDMOTHER = 'GM'
    GRANDFATHER = 'GF'
    SIBLING = 'SI'
    OTHER = 'OT'
    RELATIONSHIP_TYPE_CHOICES = (
        (MOTHER , 'Mother') ,
        (FATHER , 'Father') ,
        (GRANDMOTHER , 'Grandmother') ,
        (GRANDFATHER , 'Grandfather') ,
        (SIBLING , 'Sibling') ,
        (OTHER , 'Other') ,
    )

    family = models.ForeignKey(Family)
    phone_mobile= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    relationship = models.CharField(max_length=2,
                                    choices=RELATIONSHIP_TYPE_CHOICES,
                                    default=OTHER)

    def __unicode__(self):
        return u', '.join((unicode(self.name_family), unicode(self.name_given)))

class Member(Person):
    '''
    `Member` is a `Person` who directly participates in an `Organisation`
    '''
    class Meta:
        ordering = ['name_given', 'name_family']

    KEA = 'KE'
    CUB = 'CU'
    SCOUT = 'SC'
    VENTURER = 'VE'
    UNKNOWN = 'UK'
    MEMBERSHIP_TYPE_CHOICES = (
        (KEA , 'Kea'), 
        (CUB , 'Cub'),
        (SCOUT , 'Scout'),
        (VENTURER , 'Venturer'),
        (UNKNOWN , 'Unknown'),
    )
    organisation = models.ForeignKey(Organisation)
    sub_organistion = models.ForeignKey(SubOrganisation)
    membership_type = models.CharField(max_length=2,
                                    choices=MEMBERSHIP_TYPE_CHOICES,
                                    default=UNKNOWN)
    family = models.ForeignKey(Family)
    primary_caregiver = models.ForeignKey(Caregiver, related_name='primary_caregiver')
    caregivers = models.ManyToManyField(Caregiver, related_name='caregivers')
    date_of_birth = models.DateField()
    date_invested = models.DateField()

    def __unicode__(self):
        return u', '.join((unicode(self.name_family), unicode(self.name_given)))

