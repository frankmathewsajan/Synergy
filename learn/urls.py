from django.urls import path

from learn.views import auth, views

urlpatterns = [
    path('login/', auth.login, name='login'),
    path('forgot_password/', auth.forgot_password, name='forgot_password'),
    path('register/', auth.register, name='register'),
    path('logout/', auth.logout, name='logout'),

    path('', views.index, name='index'),
]
