from django.shortcuts import render
from .forms import UserAuthenticateForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()

def loginaccount(request):    
    if request.method == 'GET':
        return render(request, 'loginaccount.html', 
                        {'form':UserAuthenticateForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', 
                    {'form': UserAuthenticateForm, 
                    'error': 'username and password do not match'})
        else: 
            login(request,user)
            return redirect('profile')

@login_required
def logoutaccount(request):        
    logout(request)
    return redirect('home')

