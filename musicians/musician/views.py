from django.shortcuts import render,redirect
from  . models import Musician_Model
from .forms import MusicianForms
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



@method_decorator(login_required, name="dispatch"
)
class MusicianCreateView(CreateView):
    model = Musician_Model
    fields ='__all__'
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home_page')




class EditMusicianView(UpdateView):
    model = Musician_Model
    fields ='__all__'
    template_name = 'edit_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

