from django.contrib import admin
from django.urls import path,include
from . views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home_page'),
    path('add_musician/',include('musician.urls')),
    path('add_album/',include('album.urls')),
    path('',include('allauth.urls'))

]
