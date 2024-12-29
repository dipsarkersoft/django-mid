from django.urls import path,include
from .views import sign_up,profile,login_user,logout_user,password_change,password_change_without_old_pass


urlpatterns = [
   # path('',home,name='homepage'),
    path('signup/',sign_up,name='signup'),
    path('',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('profile/',profile,name='profile'),
    path('profile/changepass/',password_change,name='changepass'),
    path('profile/changepassWithOutOld',password_change_without_old_pass,name='changepassWithOutOld')
  
]
