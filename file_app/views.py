from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from .forms import FileForm, UserForm, InstitutionForm, StudentForm
from .models import Institution, Document, Student

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def presentation(request):
    return render(request,'presentation.html')


def institution_sign_up(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        institution_form = InstitutionForm(data=request.POST)

        if user_form.is_valid() and institution_form.is_valid():
            user = user_form.save()
            print(user.password)
            user.set_password(user.password)
            user.save()

            institution = institution_form.save(commit=False)
            institution.user = user
            institution.institution_id = Institution.objects.count()+1001
            institution.save()

            registered = True

            return reverse('institution_login')
        else:
            return render(request,'institution_sign_up.html',{'user_form':user_form,'institution_form':institution_form})
    else:
        user_form = UserForm()
        institution_form = InstitutionForm()
        return render(request,'institution_sign_up.html',{'user_form':user_form,'institution_form':institution_form})

def institution_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('institution_profile'))
            else:
                return render(request,'institution_login.html',{"err_message":"Invalid login. Please try again"})
        else:
            return render(request,'institution_login.html',{"err_message":"Invalid login. Please try again"})
    else:
        return render(request,'institution_login.html',)

def student_sign_up(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        student_form = StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            print(user.password)
            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.student_id = Student.objects.count()+1001
            student.save()

            registered = True

            return render(request,'student_login.html',)
        else:
            return render(request,'student_sign_up.html',{'user_form':user_form,'student_form':student_form,'err_message':"Couldn't sign you up. Please try again later"})
    else:
        user_form = UserForm()
        student_form = StudentForm()
        return render(request,'student_sign_up.html',{'user_form':user_form,'student_form':student_form})

def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('student_profile'))
            else:
                return render(request,'student_login.html',{"err_message":"Invalid login. Please try again"})
        else:
            return render(request,'student_login.html',{"err_message":"Invalid login. Please try again"})
    else:
        return render(request,'student_login.html',)

@login_required(login_url="/institution/login")
def institution_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="/student/login")
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="/institution/login")
def upload_view(request):
    if Institution.objects.filter(user = request.user).first() != None:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = FileForm(request.POST)
            # check whether it's valid:
            if form.is_valid() and Student.objects.filter(student_id=request.POST['student_id']).first()!= None:
                student = Student.objects.get(student_id=request.POST['student_id'])
                Document.objects.get_or_create(institution = Institution.objects.get(user=request.user), document_name = form.cleaned_data['document_name'],student=student, document_link=request.POST['cid'])
                return render(request,'success.html',{'document':Document.objects.get(institution = Institution.objects.get(user=request.user), document_name = form.cleaned_data['document_name'],student=student, document_link=request.POST['cid']),'student':student})
            else:
                return render(request,'upload.html', {'form': form,'institution':Institution.objects.get(user=request.user),'err_message':'Invalid receipt id'})
        # if a GET (or any other method) we'll create a blank form
        else:
            form = FileForm()
            return render(request, 'upload.html', {'form': form,'institution':Institution.objects.get(user=request.user)})
    else:
        return HttpResponseRedirect(reverse('institution_login'))


@login_required(login_url="/student/login")
def student_profile(request):
    try:
        return render(request,"student_profile.html",{'student':Student.objects.get(user=request.user)})
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse('student_login'))

@login_required(login_url="/institution/login")
def institution_profile(request):
    try:
        return render(request,"institution_profile.html",{'institution':Institution.objects.get(user=request.user)})
    except Institution.DoesNotExist:
        return HttpResponseRedirect(reverse('institution_login'))
