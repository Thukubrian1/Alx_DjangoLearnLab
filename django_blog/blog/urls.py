from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag

urlpatterns = [
    # Built-in login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), # View a single post
    path('create/', views.PostCreateView.as_view(), name='post_create'),   # Create a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', "PostByTagListView.as_view()"),
]

