from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomModel, Book
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q  # For safe query filtering
from .forms import ExampleForm  
# Create your views here.

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the form data, like saving to the database
            return render(request, 'success.html', {'name': name})
    else:
        form = ExampleForm()  # Instantiate an empty form for GET requests

    return render(request, 'example_form.html', {'form': form})
def Book_list(request):
    books = Book.objects.all()
    return render(request , "book_list.html")

def bookshelf(request):
    context = {}
    return render(request, 'index.html',context)

@permission_required('your_app_name.can_view', raise_exception=True)
def view_custom_model(request):
    objects = CustomModel.objects.all()
    return render(request, 'your_app_name/view_custom_model.html', {'objects': objects})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_custom_model(request):
    if request.method == 'POST':
        # Handle form submission to create an object
        pass
    return render(request, 'your_app_name/create_custom_model.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_custom_model(request, pk):
    obj = get_object_or_404(CustomModel, pk=pk)
    if request.method == 'POST':
        # Handle form submission to edit the object
        pass
    return render(request, 'your_app_name/edit_custom_model.html', {'object': obj})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_custom_model(request, pk):
    obj = get_object_or_404(CustomModel, pk=pk)
    if request.method == 'POST':
        obj.delete()
        # Redirect after deletion
    return render(request, 'your_app_name/delete_custom_model.html', {'object': obj})

@csrf_protect  # Enforce CSRF protection for form submissions
def secure_view(request):
    if request.method == 'POST':
        # Safely process the form data
        form_data = request.POST.get('data', '')
        if validate_input(form_data):
            # Perform actions with validated data
            return render(request, 'secure_template.html', {'data': form_data})
        else:
            return HttpResponseForbidden("Invalid input")
    return render(request, 'secure_form.html')

# Safe handling for search queries
def search_view(request):
    query = request.GET.get('q', '')
    if validate_input(query):
        results = MyModel.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return render(request, 'search_results.html', {'results': results})
    else:
        return HttpResponseForbidden("Invalid search query")

# Helper to validate user inputs
def validate_input(data):
    # Add input validation logic here
    return True if data and len(data) < 255 else False