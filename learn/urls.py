from django.urls import path
from learn.views import auth, views

urlpatterns = [
    path('login/', auth.login, name='login'),
    path('forgot_password/', auth.forgot_password, name='forgot_password'),
    path('register/', auth.register, name='register'),
    path('logout/', auth.logout, name='logout'),

    path('', views.index, name='index'),

    # Group URLs with consistent naming and trailing slashes
    path('groups/', views.groups, name='group_list'),
    path('groups/new/', views.new_group, name='group_create'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),

    # Events

    path('events/', views.events, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
]
