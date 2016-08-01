from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

class QuoteManager(models.Manager):
    def register(self, **kwargs):
        flagger = True
        errors = []
        if len(kwargs['author'][0]) == 0 or len(kwargs['quote'][0]) == 0:
            flagger = False
            errors.append("Please fill out every field!")
        if len(kwargs['author'][0]) < 3:
            flagger = False
            errors.append("'Quote By' must be longer than 3 letters!")
        if len(kwargs['quote'][0]) < 10:
            flagger = False
            errors.append("'Message:' must be longer than 10 letters!")
        return(flagger, errors)

class Quote(models.Model):
    user = models.ForeignKey(User)
    author = models.CharField(max_length=100)
    quote = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    quoteManager = QuoteManager()
    objects = models.Manager()

class Favorite(models.Model):
    user = models.ForeignKey(User)
    quote = models.ForeignKey(Quote)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
# Create your models here.
