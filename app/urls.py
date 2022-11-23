from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('add-todo/',views.add_todo,name='add_todo'),
    # re_path(r'^delete_todo/(?P<pk>[0-9]+)/$', views.delete_todo,name="delete_todo"),
    path('delete-todo/',views.delete_todo,name='delete_todo'),
    path('change-status/',views.change_status,name='change_status'),

    
]