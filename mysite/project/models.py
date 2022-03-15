from django.db import models
from users.models import User
# Create your models here.

class ProjectBefore (models.Model):

    ProID = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100 ,default='Unapprove')
    projectname = models.CharField(max_length=150)
    projectmanager= models.CharField(max_length=150)
    article = models.CharField(max_length=1500)
    PreStudentID = models.ManyToManyField(User, blank=True, related_name="PreStudentID")


class ProjectAfter (models.Model):

    CATEGORY = [
        ('OnGoing', 'OnGoing'),
        ('Complete', 'Complete'),
        ]

    ProID = models.AutoField(primary_key=True)
    status = models.BooleanField(max_length=100 ,blank=True ,choices = CATEGORY)
    projectname = models.CharField(max_length=150)
    projectmanager= models.CharField(max_length=150)
    article = models.CharField(max_length=1500)
    StudentID = models.ManyToManyField(User, blank=True, related_name="StudentID")
    TeacherID = models.ManyToManyField(User, blank=True, related_name="TeacherID")

class Comment (models.Model):

    projectcommented = models.ManyToManyField(ProjectAfter, blank=True, related_name="projectcommented")
    comment_text = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)

