from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('students/', students, name='students'),
    path('staffs/', staffs, name='staffs'),
    path('admins/', admins, name='admins'),
    path('editors/', editors, name='editors'),
    path('access-denied/', access_denied, name='access_denied'),
]
