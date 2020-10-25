from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from master.models import *


@login_required(login_url='login')
def redirect(request):
    return render(request, "profile/redirect.html")

@login_required(login_url='login')
def home(request):
    current_user = request.user

    data = Profile.objects.all()

    profile = {
        "profile_all": current_user
    }
    return render(request,"home.html",profile)