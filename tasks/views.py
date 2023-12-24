from django.shortcuts import render

# ## auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def helloworld(request):
    return render(request, 'auth/signup.html', {
      'form': UserCreationForm()
    })



def signup(request):
    return 