from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .models import ProjectBefore, ProjectAfter, User
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib import messages
# Create your views here.

class ProjectCreateView(CreateView):
    model = ProjectBefore
    fields = ('projectname', 'projectmanager', 'article')
    template_name = '../templates/project/projectcreate.html'

    def form_valid(self, form):
        project = form.save(commit=True)
        project.PreStudentID.add(self.request.user)
        project.save()
        messages.success(self.request, 'Project added Success')
        return redirect('/')
        

def PreProjectView(request):
    user = User.objects.get(request.user.username)
    return render(request, "storepage/projectview.html",{
        "projectb": ProjectBefore.objects.filter(PreStudentID=user)
    })
