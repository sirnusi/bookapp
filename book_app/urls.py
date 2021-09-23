from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book_details/<slug:slug>/', views.BookDetailView.as_view(), name='book_details'),
    path('create_books/', views.BookCreateView.as_view(), name='create_books'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('update_books/<int:pk>/', views.BookUpdateView.as_view(), name='update_books'),
    path('delete_books/<int:pk>/', views.BookDeleteView.as_view(), name='delete_books'),
    path('login/', auth_views.LoginView.as_view(template_name='book_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('books/<genre>/', views.BookGenre.as_view(), name='genre'),
    path('create_genre/', views.CreateGenre.as_view(), name='create_genre'),
    path('register_user/', views.UserRegistration.as_view(), name='register_user'),
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),
    path('send_email/', views.sendMail, name='send_email'),
]