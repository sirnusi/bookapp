from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Genre, Book, CommentBook
from .forms import BookForm, GenreForm, RegisterUser, EmailForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, reverse
# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_app/home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.request.user)
        return context


class Dashboard(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        view = HomeView.as_view(template_name='book_app/dashboard.html')
        return view(*args, **kwargs)
    
    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    
    
    def get_object(self):
        object = super().get_object()
        object.count += 1
        object.save()
        return object
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentBook.objects.filter(book=self.get_object())
        return context
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
        
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'genre', 'author', 'context', 'image']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('dashboard')


class BookGenre(ListView):
    template_name = 'book_app/book_by_genre.html'
    paginate_by = 2
    
    
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, name=self.kwargs['genre'])
        return Book.objects.filter(genre=self.genre, author=self.request.user)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = self.genre
        return context
    
    
class CreateGenre(CreateView):
    model = Genre
    form_class = GenreForm


class UserRegistration(CreateView):
    form_class = RegisterUser
    success_url = reverse_lazy('login')
    template_name = 'book_app/signup.html'


class SearchResultsView(ListView):
    model = Book
    template_name = 'book_app/search_results.html'
    
    
    def get_queryset(self):
        self.query = self.request.GET.get('q')
        object_list = Book.objects.filter(Q(title__contains=self.query))
        return object_list
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context
        
    
def sendMail(request): 
    form = EmailForm()
    messageSent = False
    
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        
        
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Sending an email with Django'
            message = cd['message']
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['recipient']])
            messageSent = True
        else:
            form = EmailForm()
            

    return render(request, 'book_app/send_email.html', {'form': form,'messageSent': messageSent})
