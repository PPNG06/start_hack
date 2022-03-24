from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Institution(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    institution_id = models.IntegerField(blank=True, null=True)
    wallet_id =models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.user.username


class Student(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    student_email = models.CharField(blank=True,null=True,max_length=1000)
    student_id = models.IntegerField(blank=True, null=True)
    student_first_name = models.CharField(max_length=100,blank=True,null=True)
    student_last_name = models.CharField(max_length=100,blank=True,null=True)
    wallet_id = models.CharField(blank=True,null=True,max_length=1000)
    def __str__(self):
        return str(self.student_first_name)+" "+str(self.student_last_name)


class Document(models.Model):
    institution = models.ForeignKey(Institution, blank=True, null=True, on_delete=models.CASCADE)
    document_name = models.CharField(blank=True, null=True, max_length=1000)
    document_link = models.CharField(blank=True, null=True, max_length=1000)
    document_hash_value = models.CharField(blank=True, null=True, max_length=1000)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.document_name
