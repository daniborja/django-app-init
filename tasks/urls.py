from django.urls import path

from . import views



urlpatterns = [

    path('', views.home, name='home'),


    path('signup/', views.signup, name='signup'),
    path('signin/', views.singin, name='login'),
    path('logout/', views.signout, name='logout'),


    path('tasks/', views.tasks, name='tasks'),

]
