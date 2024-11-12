from django.shortcuts import render
from .models import Book
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request , "relationship_app/book_list.html")


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()  
        return context