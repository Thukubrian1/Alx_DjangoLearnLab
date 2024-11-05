from django.shortcuts import render

# Create your views here.

def bookshelf(request):
    return render(request, 'bookshelf/index.html')