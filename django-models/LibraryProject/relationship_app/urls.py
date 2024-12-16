from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('relationship_app/list_books/' , view=list_books ,name='list_books'),
    path('relationship_app/library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('relationship_app/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('relationship_app/register/', views.register, name='register'),
    path('relationship_app/admin/', views.admin_view, name='admin_view'),
    path('relationship_app/librarian/', views.librarian_view, name='librarian_view'),
    path('relationship_app/member/', views.member_view, name='member_view'),
    path('relationship_app/books/add_book/', views.add_book, name='add_book'),
    path('relationship_app/books/edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('relationship_app/books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('admin-view/', views.admin_view, name='admin-view'),
    path('librarian-view/', views.librarian_view, name='librarian-view'),
    path('member-view/', views.member_view, name='member-view'),
]