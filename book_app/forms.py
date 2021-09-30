from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import Book, Genre, CommentBook


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
    message = forms.CharField(widget=forms.Textarea(attrs={'size': 40}))
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBook
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={"class": "col-sm-12"}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }
    