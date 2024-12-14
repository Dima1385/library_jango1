
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
