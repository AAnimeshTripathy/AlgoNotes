from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subject, Topic, Note, Todo, Bookmark, Blog, Comment, Tag, NoteTag, BlogTag

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

# Topic Serializer
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'name', 'description']

# Note Serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'topic', 'title', 'content', 'code_snippet', 'code_lang', 'created_at', 'updated_at']

# Todo Serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'description', 'date_created', 'date_due', 'completed', 'priority']

# Bookmark Serializer
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'title', 'url', 'notes', 'date_created', 'last_updated']

# Blog Serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content', 'summary', 'tags', 'date_created', 'last_updated']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'blog', 'content', 'date_created']

# Tag Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# NoteTag Serializer
class NoteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTag
        fields = ['id', 'note', 'tag']

# BlogTag Serializer
class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'blog', 'tag']
