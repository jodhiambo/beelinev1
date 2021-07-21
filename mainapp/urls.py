from django.urls import path
from . import views
from userprofiles.views import get_user_details

app_name="mainapp"
urlpatterns = [
    path('', views.home, name='homepage'),
    path('allcategories', views.all_categories, name='allcategories'),
    path('search', views.search_results, name='search_results'),
    path('challenges', views.challenges, name='challenges'),
    path('open-challenges', views.open_challenges, name='open-challenges'),
    path('coming-soon', views.coming_soon_challenges, name='coming-soon'),
    path('tags/<int:id>', views.tagged, name='tagged'),
    path('audiences/<int:id>', views.audience_tagged, name='audience-tagged'),
    path('submit-challenge', views.submit_a_challenge, name='submit-a-challenge'),
    path('archived-challenges', views.archived_challenges, name='archived'),
    path('rolling-challenges', views.rolling_challenges, name='rolling'),
    path('detail/<int:id>/<slug:slug>/', views.challenge_detail, name='detail'),
    path('favourite_post/<int:id>/<slug:slug>/', views.favourite_post, name='favourite_post'),
    path('interested/<int:id>/<slug:slug>', views.interested_challenges_list, name='interested-people'),
    path('favourite-challenges', views.favourite_challenge_list, name='favourite-challenges'),
    path('users/<int:id>/', get_user_details, name='the-user'),
    path('about', views.about, name="about"),
    path('privacy-policy', views.privacy_policy, name="privacy_policy"),
]
