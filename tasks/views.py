from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.db import IntegrityError


# ## auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout  # crear la auth session (cookie)


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

                # login in django (session cookie)
                login(request, user) # crea la sessionid en cookies

                return redirect('tasks')
            except IntegrityError as e: # Exception (general err)
                print(e)
                return render(request, 'auth/signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Username already exists'
                })       

        return render(request, 'auth/signup.html', {
            'form': UserCreationForm(),
            'error': 'Passwords do not match'
        }) 



def signout(request):
    logout(request)
    return redirect('home')





# ### Tasks
def tasks(request):
    return render(request, 'tasks/tasks.html')

