from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Genre
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'context', 'image')
       
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', )

class RegisterUser(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    