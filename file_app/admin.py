from django.contrib import admin
from .models import Institution, Document, Student
# Register your models here.
admin.site.register(Institution)
admin.site.register(Student)
admin.site.register(Document)
