from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from master.models import *
from .forms import *


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

@login_required(login_url='login')
def input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomNameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            room_password = form.cleaned_data['password']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomNameForm()

    return render(request, 'input.html', {'form': form})

def landingPage(request):
    return render(request,"landingPage.html")


