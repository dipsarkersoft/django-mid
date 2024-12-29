from django.urls import path,include
from .views import home,details,buy_car


urlpatterns = [
  path('',home,name='homepage'),
  path('<slug:slug>',home,name='brandWise'),
  path('details/<int:id>',details,name='details'),
  path('order/<int:id>',buy_car,name='buy_car'),
  
    
]

