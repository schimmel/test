from django.db import models

class Employee(models.Model):
    lname = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    def __unicode__(self):
        return self.fname + ' ' + self.lname

class Time(models.Model):
    emp = models.ForeignKey(Employee)
    start = models.DateTimeField('Start Time')
    end = models.DateTimeField('End Time')
    def __DateTime__(self):
        return self.start
