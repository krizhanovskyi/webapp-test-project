from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import File, FileManager, User




def home(request):
        return render(request, 'home.html')


@login_required(login_url='loginaccount')
def profile(request):
        return render(request, 'profile.html')