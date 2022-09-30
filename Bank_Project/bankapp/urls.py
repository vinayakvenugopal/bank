from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('page',views.page,name='page'),
    path('form',views.form,name='form'),
    path('reply',views.form,name='reply')
]