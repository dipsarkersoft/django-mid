from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . models import Album_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required,name='dispatch')     
class AlbumCreateView(CreateView):
    model = Album_model
    fields ='__all__'
    template_name = 'add_album.html'
    success_url = reverse_lazy('home_page')

@method_decorator(login_required,name='dispatch')
class EditAlbumView(UpdateView):
    model = Album_model
    fields ='__all__'
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@method_decorator(login_required,name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album_model
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
 
