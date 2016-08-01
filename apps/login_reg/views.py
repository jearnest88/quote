from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

#register/login page
def index(request):
    return render(request, 'login_reg/index.html')

#this registers a new user to the DB
def register(request):
    result = User.userManager.register(**request.POST)
    if result[0]:
        encoded_password = request.POST['password'].encode(encoding="utf-8", errors="strict")
        hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        User.objects.create(name=request.POST['name'], alias=request.POST['name'], email=request.POST['email'], password=hashed, birthday=request.POST['birthday'])
        messages.add_message(request, messages.SUCCESS, "User registered!")
    else:
        messages.add_message(request, messages.ERROR, result[1])
    return redirect('/')

#this checks the DB for existing user and logs in, directs them to their user page
def login(request):
    result = User.userManager.login(request.POST['email'], request.POST['password'])
    print result
    if result[0]:
        print result[1]
        request.session['user_id'] = result[1].id
        request.session['name'] = result[1].name
        return redirect('/quotes')
    else:
        messages.add_message(request, messages.ERROR, result[1])
        return redirect('/')
