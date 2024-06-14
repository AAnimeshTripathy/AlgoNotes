from django.db import models
from django.contrib.auth.models import User

# Models for storing notes

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    code_snippet = models.TextField(blank=True, null=True)

# Models for Todo list

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# Models for bookmarking questions

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    notes = models.TextField(blank=True, null=True)

# Models for blog posts

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=200, blank=True, null=True)
