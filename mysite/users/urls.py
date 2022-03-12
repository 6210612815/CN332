from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="users"


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_view, name='logout'),

]