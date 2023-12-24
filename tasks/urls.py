from django.urls import path

from . import views



urlpatterns = [

    path('', views.helloworld, name='hello_world'),

    path('signup/', views.signup, name='signup')

]
