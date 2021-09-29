from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('dashboard')
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    release_year = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    
    class Meta:
        ordering = ['-release_year']
    
    def get_absolute_url(self):
        return reverse('dashboard')
    
    def __str__(self):
        return self.title


class CommentBook(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.name