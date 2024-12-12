from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomModel

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
 
    list_display = ('title', 'author', 'publication_year')  
    list_filter = ('author', 'publication_year') 
    search_fields = ('title', 'author') 

admin.site.register(Book,BookAdmin)

class CustomUserAdmin(UserAdmin):
    """Admin configuration for the custom user model."""

    model = CustomUser
    fieldsets = (
        (None, {"fields": ("username", "password")} ),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")} ),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")} ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")} ),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )

    list_display = ["username", "email", "first_name", "last_name", "is_staff", "date_of_birth"]
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    class CustomModelAdmin(admin.ModelAdmin):
        """Admin configuration for CustomModel with permissions."""
    list_display = ("name", "description")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomModel, CustomModelAdmin)