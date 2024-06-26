from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import forms
from django.contrib.auth import login, logout
import json
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from subscriptions.models import Subscription


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:    
        form = forms.CustomUserCreationForm()
    return render(request, 'users/register.html',{ 'form': form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print(form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html',{ 'form': form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

@login_required(login_url="/users/login/")
def user_profile_view(request,user_id):

    # if no matching user is foud, redirect to 404.
    user = get_object_or_404(User, id= user_id)
    my_subs = Subscription.objects.filter(pub = user)
    my_pubs = Subscription.objects.filter(sub = user)

    # user is found!
    # username = user.username
    # firstname = user.first_name
    # lastname = user.last_name

    return render(request, 'users/user_profile.html',{'user_viewed':user,'subs':my_subs, 'pubs':my_pubs})
