from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name , self.author
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length= 100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name , self.books

class Librarian(models.Model):
    name = models.CharField(max_length= 50)
    library = models.OneToOneField(Library,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name ,self.library
    

# Define User Roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# Signal to automatically create or update the UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()