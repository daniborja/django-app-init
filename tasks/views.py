from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


# ## auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout  # crear la auth session (cookie)


# ## models: user is provided by django by default
from django.contrib.auth.models import User
from .models import Task


# ## forms:
from .forms import TaskForm



# Create your views here.

def home(request):
    return render(request, 'home/home.html')



# ### Auth
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



def singin(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html', {
            'form': AuthenticationForm()
        })
    else:
        # validate user data (if it exists in db and is correct password) retur user
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'auth/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user) # create session and sessionid in cookies
            return redirect('tasks')



def signout(request):
    logout(request)
    return redirect('home')





# ### Tasks
def tasks(request):
    tasks_db = Task.objects.filter(user_id = request.user.id)
    return render(request, 'tasks/tasks.html', {
            'tasks': tasks_db
        }
    )


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': TaskForm()
        })
    else:
        try:
            # ## Create task
            new_task = TaskForm(request.POST).save(commit=False)
            new_task.user = request.user  # login() set user in request
            new_task.save() # persist in db

            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/create_task.html', {
                'form': TaskForm(),
                'error': 'Please provide valid data'
            })


def task(request, id):
    # validate that the task belongs to authUser
    task_db = get_object_or_404(Task, id=id, user_id=request.user.id)

    if request.method == 'GET':
        form = TaskForm(instance=task_db)
        return render(request, 'tasks/task.html', {
            'task': task_db,
            'form': form
        })
    else:
        try:
            # ### upd task
            updated_task = TaskForm(request.POST, instance=task_db)
            updated_task.save()
            return redirect('tasks')
        except:
            return render(request, 'tasks/task.html', {
                'form': TaskForm(),
                'error': 'Please provide valid data'
            })

