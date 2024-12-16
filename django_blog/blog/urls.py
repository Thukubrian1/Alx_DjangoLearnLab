from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag

urlpatterns = [
    # Built-in login and logout views
    path('', views.HomeView.as_view(), name='home'),
    path('blog/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('blog/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blog/register/', views.register, name='register'),
    path('blog/profile/', views.profile, name='profile'),
    path('blog/posts/', PostListView.as_view(), name='posts'),
    path('blog/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/posts/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/create/', views.PostCreateView.as_view(), name='post_create'),   # Create a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('blog/posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('blog/posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('blog/post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/',PostUpdateView.as_view()),
    path('blog/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('blog/search/', search_posts, name='search-posts'),

]

