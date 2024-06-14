
from django.urls import path
from . import views

urlpatterns = [
    # URLs for subjects
    path('subjects/', views.SubjectListCreateAPIView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name='subject-detail'),

    # URLs for topics
    path('topics/', views.TopicListCreateAPIView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', views.TopicRetrieveUpdateDestroyAPIView.as_view(), name='topic-detail'),

    # URLs for notes
    path('notes/', views.NoteListCreateAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),

    # URLs for todo items
    path('todos/', views.TodoListCreateAPIView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),

    # URLs for bookmarks
    path('bookmarks/', views.BookmarkListCreateAPIView.as_view(), name='bookmark-list'),
    path('bookmarks/<int:pk>/', views.BookmarkRetrieveUpdateDestroyAPIView.as_view(), name='bookmark-detail'),

    # URLs for blog posts
    path('blogs/', views.BlogListCreateAPIView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
]
