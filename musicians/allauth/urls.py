from django.urls import path,include
from .views import UserLoginView,sign_up,profile,logout_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
   path('signup/',sign_up,name='signup'),
   path('login/', UserLoginView.as_view() ,name='login'),
   path('profile/',profile,name='profile'),
   path('logout/',LogoutView.as_view(),name='logout'),
   
  
   

]
