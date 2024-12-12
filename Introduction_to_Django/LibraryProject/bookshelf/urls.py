from django.urls import path
from .views import bookshelf

urlpatterns = [
    path("", view = bookshelf, name="bookshelf"),
]
