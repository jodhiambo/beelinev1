from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from userprofiles.views import get_users_list, get_user_details

app_name = 'users'
urlpatterns = [
    path('accounts/signup/', views.MySignUpView.as_view(), name='account_signup'),
    path('accounts/login/', views.MyLoginView.as_view(), name='account_login'),
    # path('users/list/', get_users_list, name='userlist'),
    # path('users/<int:id>/', get_user_details, name='the-user'),
    ]
