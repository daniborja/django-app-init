from django.urls import path

from . import views



urlpatterns = [

    path('', views.home, name='home'),


    path('signup/', views.signup, name='signup'),
    path('signin/', views.singin, name='login'),
    path('logout/', views.signout, name='logout'),


    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create', views.create_task, name='create_task'),
    path('tasks/complete/<int:id>', views.complete_task, name='complete_task'),
    path('tasks/<int:id>', views.task, name='task'), # URL Params - al final

]
