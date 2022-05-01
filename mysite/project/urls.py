from django.urls import path
from . import views

app_name="project"


urlpatterns = [
    path('create_project', views.ProjectCreateView.as_view(), name='create_project'),
    #path('view_project', views.PreProjectView, name='view_project'),
    path('comment_project', views.CommentCreateView , name='comment_project' ),

]