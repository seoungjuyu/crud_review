
from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('join-up/', views.join_up, name='join-up'),
    path('log-on/', views.log_on, name='log-on'),
]