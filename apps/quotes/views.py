from django.shortcuts import render, redirect, HttpResponse
from ..login_reg.models import User
from .models import Quote, Favorite
from django.contrib import messages
import bcrypt

def index(request):
    favorite = Favorite.objects.filter(user=request.session['user_id'])
    fav = Favorite.objects.filter(user=request.session['user_id']).values('quote')
    quote = Quote.objects.exclude(id__in=fav)
    context = {
    "quotes": quote,
    "users": User.objects.all(),
    "favorites": favorite
    }
    return render(request,'quotes/index.html', context)

def register_quote(request):
    user = User.objects.filter(id=request.session['user_id'])
    result = Quote.quoteManager.register(**request.POST)
    if result[0]:
        Quote.objects.create(user=user[0], author=request.POST['author'], quote=request.POST['quote'])
        messages.add_message(request, messages.SUCCESS, "Quote Posted!")
    else:
        messages.add_message(request, messages.ERROR, result[1])
    return redirect('/quotes')

def favorite(request, id):
    user = User.objects.filter(id=request.session['user_id'])
    fav_quote = Quote.objects.filter(id=id)
    Favorite.objects.create(user=user[0], quote=fav_quote[0])
    return redirect('/quotes')

def destroy(request, id):
    favorite = Favorite.objects.get(id=id)
    favorite.delete()
    return redirect('/quotes')

def userpage(request, id):
    user = User.objects.get(id=id)
    quote = Quote.objects.filter(user=id)
    count = Quote.objects.filter(user=id).count()
    context = {
    'name': user.name,
    'quotes': quote,
    'count': count
    }
    return render(request, 'quotes/userpage.html', context)
