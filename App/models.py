from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator,MinValueValidator

class Catelogue(models.Model):
    name = models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    created_date = models.DateField(max_length=15)
    class Meta:
        ordering = ('branch','created_date',)
    def __unicode__(self):
        return self.name


class Course(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name= models.CharField(max_length=30)
    code=models.CharField(max_length=9, unique=True, validators=[alphanumeric])
    category=models.CharField(max_length=3)
    credits=models.PositiveIntegerField()
    cat=models.ForeignKey(Catelogue)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=30)
    user = models.ForeignKey(User)
    pin=models.PositiveIntegerField()
    dept=models.CharField(max_length=3)
    section=models.CharField(max_length=1)
    poll=models.BooleanField()
    def __unicode__(self):
        return self.name

class Faculty(models.Model):
    user = models.ForeignKey(User)
    name=models.CharField(max_length=30)
    dept=models.CharField(max_length=3)
    pin=models.PositiveIntegerField()
    #subject=models.ForeignKey(Course)
    def __unicode__(self):
        return self.name


class Choice(models.Model):
    catelogue=models.ForeignKey(Catelogue)
    course=models.ForeignKey(Course)
    votes=models.IntegerField(default=0)

#Catelogue.courses.through.__unicode__= lambda x:x.course.name
