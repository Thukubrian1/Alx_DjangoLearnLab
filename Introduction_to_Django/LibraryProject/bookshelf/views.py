from django.shortcuts import render

# Create your views here.

def bookshelf(request):
    context = {}
    return render(request, 'index.html',context)