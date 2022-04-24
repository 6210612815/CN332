from nntplib import ArticleInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from project.models import ProjectBefore, ProjectAfter, User
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

# Create your views here.

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/users/login.html',
    context={'form':AuthenticationForm()})


def index(request):
    if request.user.is_authenticated:
        return render(request, '../templates/users/index.html',)
    else:
        return redirect('/login')

def logout_view(request):
    logout(request)
    return redirect("/")

def approval(request):
    return render(request, "users/projectapproval.html",{
        "projectb": ProjectBefore.objects.all()
    })

def approved(request, ProID):
    projectid = ProID
    return render(request, "users/projectcheck.html",{
        "project": ProjectBefore.objects.filter(ProID=projectid)
    })

def checkapprove(request, ProID):
    user = User.objects.get(username = request.user.username)
    projectid = ProID
    bproject = ProjectBefore.objects.get(ProID = projectid)

    aproject = ProjectAfter.objects.create(
        projectname = bproject.projectname,
        projectmanager = bproject.projectmanager,
        article = bproject.article,
        )

    for owner in ProjectBefore.objects.get(pk=ProID, ProID = projectid).PreStudentID.all():
            aproject.StudentID.add(owner)

    aproject.TeacherID.add(user)
    return render(request, "users/projectcheck.html",{
        "project": ProjectBefore.objects.filter(ProID=projectid)
    })

def checkcomment(request, ProID):
    user = User.objects.get(username = request.user.username)
    projectid = ProID
    project = ProjectAfter.objects.get(ProID = projectid)

    return render(request, "users/projectcommented.html",{
        "project": ProjectAfter.objects.filter(ProID=projectid)
    })

def commented(request, ProID):
    projectid = ProID
    return render(request, "users/projectcommented.html",{
        "project": ProjectAfter.objects.filter(ProID=projectid)
    })

def status(request):
    user = User.objects.get(username = request.user.username)
    return render(request, "users/projectstatus.html",{
        "projectb": ProjectBefore.objects.filter(PreStudentID=user)
    })

def submit(request):
    return render(request, "users/projectsubmit.html",{
        "project": ProjectAfter.objects.all()
    })

def update(request):
    return render(request, '../templates/users/projectupdate.html',)


