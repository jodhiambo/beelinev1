from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# from mainapp import admin
from graphene_django.views import GraphQLView
from mainapp.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('accounts/', include('allauth.urls')),
    path('', include('mainapp.urls')),
    path('', include('userprofiles.urls')),
    path('', include('news.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
# handler500 = views.page_500_not_found
# handler404 = 'mainapp.views.error_404'
# handler500 = 'mainapp.views.error_500'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
