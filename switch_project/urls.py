"""switch_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from file_app.views import home, presentation, upload_view, institution_sign_up, institution_login, institution_profile, institution_logout, student_sign_up, student_login,student_profile, student_logout, certificate_check
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("about",presentation,name="presentation"),
    path("institution/upload",upload_view,name="upload"),
    path("institution/sign_up",institution_sign_up,name="institution_sign_up"),
    path("institution/login",institution_login,name="institution_login"),
    path("institution/logout",institution_logout,name="institution_logout"),
    path("institution",institution_profile,name="institution_profile"),
    path("student",student_profile,name="student_profile"),
    path("student/sign_up",student_sign_up,name="student_sign_up"),
    path("student/login",student_login,name="student_login"),
    path("student/logout",student_logout,name="student_logout"),
    path("certificate/check",certificate_check,name="certificate_check"),
]
