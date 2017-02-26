from django.contrib.auth.models import User
from django.forms import ModelForm
from models import *
from datetime import date
from django.forms.widgets import TextInput, Select
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name','pin','dept','section')
        exclude=('poll',)

class FacultyForm(ModelForm):
    class Meta:
        model=Faculty
        fields=('name','dept','pin')

class CourseForm(ModelForm):
    class Meta:
        model=Course
        fields =('name','code','category','credits')
        exclude=('cat',)

class CatelogueForm(ModelForm):
    class Meta:
        model=Catelogue
        fields=('name','branch','created_date')