from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news', views.news_view, name='news'),
    path('news/<int:id>/<slug:slug>/', views.news_details_page, name='details'),
]