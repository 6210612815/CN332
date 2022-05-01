from audioop import reverse
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .models import ProjectBefore, ProjectAfter, User , Comment
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib import messages
from django.urls import reverse

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

def CommentCreateView(request):
    if request.method == "POST":
        text = request.POST["comment_text"]
        rating = request.POST["rating"]
        store_comment = Comment(comment_text=text,rating=rating)
        store_comment.save()
        return HttpResponseRedirect(reverse("users:update"))
    return render(request, "../templates/project/projectcomment.html")
