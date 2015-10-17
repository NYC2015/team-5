from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

import json
import sys

from models import *


# Create your views here.


VENDOR="vendor"
USER="user"


def createUser(request):
    """CREATES A USER """

    """Get all user input data"""
    username = request.POST['username']
    password = request.POST['password']
    snapAcc = request.POST["snap"]
    print username, password, snapAcc
    user = User.objects.create_user(username, None, password)
    user.save()
    customer = Customers(snap = snapAcc, username=user, distance_rad=5, home_loc="" )
    customer.save()
    print username, password
    return render(request, "FeedTheChildren/userSettings.html")

def loginUser(request):

    """Log in the user"""
    username = request.POST["username1"]
    password = request.POST["password1"]
    print username
    print password
    user = authenticate(username=username, password=password)
    print "break"
    if user is not None:
        if user.is_active:
             login(request, user)
             print "break"
	     return render(request, "FeedTheChildren/userHome.html")
    	else:
	     print "Not an Active User"

    else:     
        print "there is no such user"

    return render(request, "FeedTheChildren/index.html")


def home(request):
    return render(request, "FeedTheChildren/index.html")

