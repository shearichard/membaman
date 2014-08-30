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
        return unicode(self.name)

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
        ordering = ['start', 'end']

    year = models.ForeignKey(Year)
    name = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return unicode(self.name)

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
        ordering = ['subyear__start', 'subyear__end']

    subyear = models.ForeignKey(SubYear)
    member = models.ForeignKey(Member)
    received = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.received)
