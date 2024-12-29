from django.urls import path,include
from .views import EditAlbumView,AlbumCreateView,DeleteAlbumView

urlpatterns = [
   
   path('add/',AlbumCreateView.as_view(),name='add_albums'),
   path('edit/<int:id>',EditAlbumView.as_view(),name='edit_albums'),
   path('del/<int:id>',DeleteAlbumView.as_view(),name='del_albums')
   

]