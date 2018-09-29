# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import re, bcrypt

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = False
        # return redirect('books:index')
        return render(request, 'reviewer/index.html')

    if 'logged_in' not in request.session:
        # return redirect('users:new')
        request.session['logged_in'] = False
        return render(request, 'reviewer/index.html')
    else:
        return redirect('/books')


def new(request):
    # if 'user_id' not in request.session:
    #     request.session['user_id'] = False
    # if 'logged_in' not in request.session:
    #     request.session['logged_in'] = False
    context = {}
    return render(request, 'reviewer/new.html', context)

def register(request):
    if request.method == 'POST':
        valid, result = User.objects.validate_and_create_user(request.POST)
        if not valid:
            for error in result:
                messages.error(request, error)
            return redirect('users:new')
        request.session['user_id'] = result
        request.session['logged_in'] = valid
        print "Session User ID:", result
        print "Login status:", request.session['logged_in']
        return redirect('users:index')
    else:
        return redirect('users:new')


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
        return redirect('books:index')

def books(request):

    return render(request, 'reviewer/books.html')

def addbooks(request):

    return render(request, 'reviewer/addbook.html')

def addbookprocess(request, book_id):
    pass

def showbook(request, book_id):
    context = {}
    return render(request, 'reviewer/books.html', context)

def delete(request, user_id):
    if request.method == 'POST':
        User.objects.delete_user_by_id(user_id)
    return redirect('users:index')
    
def logout(request):
    request.session.clear()
    return redirect('users:index')