# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import re, bcrypt
from ..users.models import User

# Create your models here.
class BookManager(models.Manager):
    def create_book_and_review(self, form_data):
        errors = []
        name = form_data['title']
        # teacher = form_data['teacher']

        if len(title) < 5:
            errors.append('Book title must be at least 5 characters.')
        try:
            book = Book.objects.get(id=form_data['title'])
            # if teacher.permission_level != 'TEACHER':
            #     errors.append("Selected teacher invalid.")
        except:
            errors.append("Some error to go here")

        if errors:
            return (False, errors)
        else:
            book = Book.objects.create(name=name, author=author, review=review)
            return (True, course)

    def review_validator(self, form_data):
        errors = []
        review = form_data['review']

        if len(review) < 10:
            errors.append('Review must be at least 10 characters.')

class Book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

def __str__(self):
    output = "<Book object: {} {} {}>".format(self.title, self.author, self.review)
    return self.output

class Review(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    review = models.TextField()
    user = models.ForeignKey(User, related_name="user_reviews")
    book = models.ForeignKey(Book, related_name="book_reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    output = "<Review object: {} {}>".format(self.rating, self.review)
    return self.output

class Author(models.Model):
    name = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    output = "<Author object: {} {}>".format(self.name, self.books)
    return self.output