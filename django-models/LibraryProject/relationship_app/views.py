from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request , "relationship_app/list_books.html")


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, request, **kwargs):

        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()   
        return render(request, 'relationship_app/list_books.html', context)


from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Custom Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Helper functions to check roles
def Admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def Librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def Member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view
@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view
@user_passes_test(Member)
def member_view(request):
    return render(request, 'member_view.html')