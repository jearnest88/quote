from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, **kwargs):
        flagger = True
        errors = []
        if len(kwargs['name'][0]) == 0 or len(kwargs['alias'][0]) == 0 or len(kwargs['email'][0]) == 0 or len(kwargs['password'][0]) == 0 or len(kwargs['confirm_pw'][0]) == 0:
            flagger = False
            errors.append("Please fill out every field!")
        if not EMAIL_REGEX.match(str(kwargs['email'][0])):
            print(str(kwargs['email'][0]))
            flagger = False
            errors.append("Email is not in a valid format!")
        if kwargs['password'][0] != kwargs['confirm_pw'][0]:
            flagger = False
            errors.append('Password and Confirm PW must match!')
        return (flagger, errors)

    def login(self, email, password):
        try:
            user = User.objects.get(email=email)
            print('user?', user.email, user.password)
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print('pw matched!')
                return(True, user)
            else:
                return(False, 'Login incorrect!')

        except:
            return(False, 'Login incorrect!')

class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()
