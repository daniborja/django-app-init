from django.shortcuts import render, redirect

from django.http import HttpResponse


# ## auth
from django.contrib.auth.forms import UserCreationForm


# ## models: user is provided by django by default
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    return render(request, 'home/home.html')



def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm()
        })
    else:
        # ## POST: persistir en DB
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                return redirect('home')
            except Exception as e:
                print(e)
                return HttpResponse('Username already exists')
        
        return HttpResponse('Invalid Password')

