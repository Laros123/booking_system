from django.urls import path
from auth_system.views import register, login_user, logout_user, profile, ukrainian, english

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('ukrainian', ukrainian, name='ukrainian'),
    path('english', english, name='english'),
    path('logout', logout_user, name='logout'),
    path('profile', profile, name='profile')
]