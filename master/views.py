from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def redirect(request):
    return render(request, "profile/redirect.html")

def home(request):
    return render(request,"home.html")