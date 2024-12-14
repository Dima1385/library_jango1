from django.shortcuts import render, redirect

def home(request):
    return render(request, 'library/home.html')

def books_view(request):

    books = ['Книга 1', 'Книга 2', 'Книга 3']
    return render(request, 'library/books.html', {'books': books})

def login_view(request):
    return render(request, 'library/login.html')

def register_view(request):
    return render(request, 'library/register.html')
