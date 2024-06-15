from django.db import models
from django.contrib.auth.models import User

# Models for storing notes

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Added description field

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Added description field

    def __str__(self):
        return self.name

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    code_snippet = models.TextField(blank=True, null=True)
    code_lang = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Added timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)      # Added timestamp for updates

    def __str__(self):
        return self.title

# Models for Todo list

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)  # Added priority field

    def __str__(self):
        return self.description

# Models for bookmarking questions

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)  # Added timestamp for creation
    last_updated = models.DateTimeField(auto_now=True)      # Added timestamp for updates

    def __str__(self):
        return self.title

# Models for blog posts

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.CharField(max_length=500, blank=True, null=True)  # Added summary field
    tags = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)  # Added timestamp for creation
    last_updated = models.DateTimeField(auto_now=True)      # Added timestamp for updates

    def __str__(self):
        return self.title

# Models for comments

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'

# Models for tags

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NoteTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
