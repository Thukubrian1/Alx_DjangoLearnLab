from django.shortcuts import get_object_or_404, render , redirect
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'relationship_app/book_list.html', {'page_obj': page_obj})


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
        return render(request, 'relationship_app/list_books.html')


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
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        if Book.is_valid():
            Book.save()
            return redirect('book_list')  # redirect to the book list after adding
    else: 
        return render(request, 'relationship_app/add_book.html',)

@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = Book(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        return render(request, 'edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('relationship_app/book_list')