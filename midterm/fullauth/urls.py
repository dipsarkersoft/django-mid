
from django.contrib import admin
from django.urls import path
from .views import sign_up,UserLoginView,profile,editProfile,AllOrderView,PassChangeView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('signup/',sign_up,name='signup'),
   path('profile/',profile,name='profile'),
   path('profile/order',AllOrderView.as_view(),name='allorder'),
   path('profile/edit/',editProfile,name='editProfile'),
   path('profile/passChange',PassChangeView.as_view(),name='passChange'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('login/',UserLoginView.as_view(),name='login'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)