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
    path('books_genre/<genre>/', views.BookGenre.as_view(), name='genre'),
    path('create_genre/', views.CreateGenre.as_view(), name='create_genre'),
    path('register_user/', views.UserRegistration.as_view(), name='register_user'),
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),
    path('send_email/', views.sendMail, name='send_email'),
    path('comments/<int:id>/', views.CommentView.as_view(), name='new_comment'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='book_app/password_reset_form.html'), name='password_reset'),
    path('reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='book_app/password_reset_done.html'), name='password_reset_done'),
    path('reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='book_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='book_app/password_reset_complete.html'), name='password_reset_complete'),
]

