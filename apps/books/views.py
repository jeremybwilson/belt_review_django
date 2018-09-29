# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..users.models import User
from .models import Book, Review, Author

# Create your views here.
def index(request):

    if 'logged_in' not in request.session:
        return redirect('/initialize')
    else:
        if request.session['logged_in'] == True:
            return redirect('/books')
        else:
            return render(request, 'books/index.html')

def initialize(request):
    request.session["user_id"] = 0
    request.session['logged_in'] = False
    return redirect("/")


def book(request):
    # Login status check
    if request.session['logged_in'] == False:
        errors.append( "Login Fail, please login again!")
        return redirect('/')
    else:
        context ={
            'logged_in': request.session['logged_in'],
            'user_name' : User.objects.get(id=request.session['user_id']).name,
            'reviews' : Review.objects.raw("SELECT * FROM books_Review ORDER BY created_at DESC LIMIT 3"),
            'books' : Book.objects.all().order_by("-created_at"),
        }
        return render(request, "books/books.html", context)

def showbook(request, book_id):
    # check session variable to get logged_in status
    if request.session['logged_in'] == False:
        errors.append("Login Fail, please login again!")
        return redirect("/")
    else:
        context = {
            "book_id": book_id,
            "book_name": Book.objects.get(id=book_id).name,
            "book_authors": Book.objects.get(id=book_id).authors.all(),
            "login_id": request.session['user_id'],
            'reviewer': User.objects.get(id=request.session['user_id']),
            'reviews': Review.objects.filter(book = Book.objects.get(id=book_id)).order_by("-created_at"),
        }
        return render(request, "books/showbook.html", context)

def add(request):
    if request.session['logged_in'] == False:
        errors.append('Login failed, please login again!')
        return redirect("/")
    else:
        context = {
            'authors' : Author.objects.all(),
        }
        return render(request, 'books/addbook.html', context)

def addbookreviewprocess(request):
    if request.session['logged_in'] == False:
        messages.error(request, 'Login failed, please login again!')
        return redirect("/")
    else:
        errors = []
        title = request.POST['title']
        new_author = request.POST['new_author']
        rating = request.POST['rating']
        review = request.POST['review']

        user_id = int(request.session['user_id'])
        # Case : title not entered
        if len(title) < 1:
            messages.error(request, "Please enter your book title (Not accepted blank book title")
            return redirect("/books/add")
        else:
            # Case : book title is exists - use database data
            if len(Book.objects.filter(name=title)) > 0:
                book = Book.objects.get(name=title)
            # Case : new book title
            else:
                Book.objects.create(name=title)
                book = Book.objects.get(name=title)
            
            # Case : new author - typed
            if new_author != u"":

                # Case : if typed new author does not exist in database - create new author
                if len(Author.objects.filter(name=new_author)) < 1:
                    Author.objects.create(name=new_author)
                    author = Author.objects.get(name=new_author)
                    author.books.add(book)
                    author.save()
                # Case : if typed new author already exists in database - use database author
                else:
                    author = Author.objects.get(name=new_author)
                    author.books.add(book)
                    author.save()

            # Case : new author - not typed - use exist_author data
            else:
                author = Author.objects.get(name=request.POST["exist_author"])
                author.books.add(book)
                author.save()

            # Create review
            Review.objects.create(rating=rating, review=review, user = User.objects.get(id=user_id), book=book)
            return redirect("/books/" + str(book.id))

def addreviewprocess(request, book_id):
    user_id = int(request.session['user_id'])
    rating = request.POST['rating']
    review = request.POST['review']
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    Review.objects.create(rating=rating, review=review, user=user, book=book)
    return redirect("/books/" + str(book_id))

def deletereview(request, review_id):
    book_id = Review.objects.get(id=review_id).book.id
    Review.objects.get(id=review_id).delete()
    return redirect("/books/"+str(book_id))

def delete(request, user_id):
    if request.method == 'POST':
        User.objects.delete_user_by_id(user_id)
    return redirect('users:index')