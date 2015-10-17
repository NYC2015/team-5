from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from models import *
# Create your views here.

VENDOR="vendor"
USER="user"

def createUser(request):
    """CREATES A USER """

    """Get all user input data"""
    username = request.POST["Username"]
    password = request.POST["Password"]
    snapAcc = request.POST["Snap"]
	
    user = User.objects.create_user(username, None, password)
    user.save()
    customer = Customer(snap = snapAcc, username=user, p_type=USER, distance_rad=5, home_loc="" )
    customer.save()
    


def login(request):

    """Log in the user"""
    username = request.POST["Username"]
    password = request.POST["Password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
             login(request, user)
    	else:
	     print "Not an Active User"

    else:     
        print "there is no such user"




def home(request):
    return render(request, "FeedTheChildren/index.html")

    
