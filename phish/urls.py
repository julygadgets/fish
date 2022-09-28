from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',index),
    path('netflix/',netflix),
    path("dropbox/",dropbox),
    path("snapchat/",snapchat),
    path("github/",github),
    path("facebook/",facebook_mobile),]

urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

