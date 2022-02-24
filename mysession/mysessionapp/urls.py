from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('set-cookie',views.set_cookies,name='set-cookie'),
    path('get-cookie',views.get_cookies,name='get-cookie'),
    path('delete-cookie',views.del_cookies,name='delete-cookie'),
    path('set-session',views.session_set,name='set-session'),
    path('get-session',views.session_get,name='get-session'),
    path('delete-session',views.session_delete,name='delete-session')

]
