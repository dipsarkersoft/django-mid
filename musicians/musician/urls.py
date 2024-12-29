from django.urls import path,include
from .views import MusicianCreateView,EditMusicianView

urlpatterns = [
   
   path('add/',MusicianCreateView.as_view(),name='add_musicians'),
   path('edit/<int:id>',EditMusicianView.as_view(),name='edit_musicians'),
  
   
  
   

]
