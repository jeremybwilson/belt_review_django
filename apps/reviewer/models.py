# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# import re, bcrypt

# Create your models here.
# class BookManager(models.Manager):
#     def book_validator(self, form_data):
#         errors = []

#     def review_validator(self, form_data):
#         errors = []
#         review = form_data['review']

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     review = models.CharField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = BookManager()


# class Review(models.Model):
#     pass 

# class User(models.Model):
#     name = models.CharField(max_length=255)
#     alias = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     pw_hash = models.CharField(max_length=500)
#     # For permission level, admin is 1 and non-admin is 2.
#     permission_level = models.IntegerField(default=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()

# def __str__(self):
#     output = "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email, self.permission_level)
#     return self.output