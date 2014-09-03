from django.db import models

from members.models import Organisation
from members.models import Member

# Create your models here.
class Year(models.Model):
    '''
    A `Year` models a single year  
    of an `Organisation` activity
    
    '''
    class Meta:
        ordering = ['start', 'end']

    organisation = models.ForeignKey(Organisation)
    name = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return unicode(self.name) + unicode(' (') +  unicode(self.organisation.name) + unicode(')')

class SubYear(models.Model):
    '''
    A fraction of the `Year` model  

    There should be sufficient `SubYear`
    instances with suitable start end
    dates so that the whole year is covered
    with no gaps.

    In some cases a SubYear will be a 1-1
    with Year depending on how the `Organisation`
    does their billing.
    
    '''
    class Meta:
        ordering = ['year__organisation__name','start', 'end']

    year = models.ForeignKey(Year)
    name = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def year_name(self):
        return self.year.name
    year_name.short_description = 'Year Name'

    def organisation_name(self):
        return self.year.organisation
    year_name.short_description = 'Organisation Name'

    def __unicode__(self):
        return unicode(self.name) + unicode(' (') +  unicode(self.year.organisation.name) + unicode(' - ') + unicode(self.year.name) + unicode(')')

class Income(models.Model):
    '''
    `Income` represents the income from a `Member`
    based for a given `SubYear`
    
    Initially the model will just be a string 
    to contain the non-numeric values that have
    been entered into the data that's being converted
    from but in the longer term this model will take 
    on a more typed form
    '''
    class Meta:
        ordering = ['member__name_family','member__name_given','subyear__start', 'subyear__end']

    subyear = models.ForeignKey(SubYear)
    member = models.ForeignKey(Member)
    received = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(' (') + unicode(self.subyear.year.name) + unicode(' - ')+ unicode(self.subyear.name) + unicode(':') + unicode(self.member) + unicode(')') + unicode(self.received)
