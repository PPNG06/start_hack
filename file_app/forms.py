from django import forms
from django.contrib.auth.models import User
from .models import Institution, Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')

class InstitutionForm(forms.ModelForm):
    class Meta():
        model = Institution
        fields = ('wallet_id',)

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('student_first_name','student_last_name', 'student_email','wallet_id')

class FileForm(forms.Form):
    document_name = forms.CharField(label="Document name ",max_length=200)
    student_id = forms.IntegerField(label="Student id ")
