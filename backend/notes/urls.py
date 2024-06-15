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

    # URLs for comments
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    # URLs for tags
    path('tags/', views.TagListCreateAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', views.TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    # URLs for note tags
    path('notetags/', views.NoteTagListCreateAPIView.as_view(), name='notetag-list'),
    path('notetags/<int:pk>/', views.NoteTagRetrieveUpdateDestroyAPIView.as_view(), name='notetag-detail'),

    # URLs for blog tags
    path('blogtags/', views.BlogTagListCreateAPIView.as_view(), name='blogtag-list'),
    path('blogtags/<int:pk>/', views.BlogTagRetrieveUpdateDestroyAPIView.as_view(), name='blogtag-detail'),
]
