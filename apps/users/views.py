# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from ..books.models import Book, Review, Author

# Create your views here.
def index(request):
    if 'logged_in' not in request.session:
        return redirect('books:index')

    if 'user_id' not in request.session:
        return redirect('books:index')
    
    user_id = request.session['user_id']
    print "*" * 80
    print "UserID from session is:", user_id
    return redirect('/user/'+str(user_id))

def register(request):
    if request.method == 'POST':
        valid, result = User.objects.validate_and_create_user(request.POST)

        if not valid:
            for error in result:
                messages.error(request, error)
            return redirect('/')
        # else:   # case successful login
        request.session['user_id'] = result
        request.session['logged_in'] = valid
        print "*" * 80
        print "Session User ID:", result
        print "Logged in status:", valid
        return redirect('books:books')
    else:
        return redirect('books:index')

def showuser(request, user_id):
    if request.session['logged_in'] == False:
        errors.append("Login Fail, please login again!")
        return redirect("/")
    else:
        context = {
            # 'user_id': User.objects.get(id=user_id),
            'user': User.objects.get(id=user_id),
            'total_review': User.objects.get(id=user_id).user_reviews.all().count(),
            'reviews': User.objects.get(id=user_id).user_reviews.all(),
        }
        return render(request, "users/showuser.html", context)

def login(request):
    if request.method != 'POST':
        return redirect('books:index')

    valid, result = User.objects.login_user(request.POST)

    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('books:index')
    else:   # Case : successful login 
        request.session['user_id'] = result
        request.session['logged_in'] = valid
        print "*" * 80
        print "Session user_id:", result
        print "Login status:", valid
        return redirect('/books')
    
def logout(request):
    request.session.clear()
    return redirect('books:index')