from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views
# we import PostListView class from view.py
# this class have inbiult fun as_view()
urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    #path('search/',views.search,name="post-search"),
    #path('search/',views.search,name="post-search"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    #path('post/profile/<int:id>/', views.profile, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    #path('post/new', PostCreateView.as_view(), name='post-detail'),
    #path("blogPost/<int:pk>", views.blogPost, name="blog-Post"),
    #path('about/', views.about, name='blog-about'),
]
