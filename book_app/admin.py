from django.contrib import admin
from .models import Genre, Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Genre)
admin.site.register(Book, BookAdmin)