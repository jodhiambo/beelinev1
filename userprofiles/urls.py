from django.urls import path
from . import views

app_name='userprofiles'
urlpatterns = [
    path('profile', views.profile, name='profile')
]
