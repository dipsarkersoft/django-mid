from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignUp_Form
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from album.models import Album_model


# Create your views here.

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUp_Form(request.POST)
            if form.is_valid():
                messages.success(request,'SignUp Suceess')
                form.save()
                return redirect('login')

        else:
            form=SignUp_Form()
        return render(request,'signuppage.html',{'form':form})
    else:
        return redirect('profile')



class UserLoginView(LoginView):
    template_name = 'loginPage.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def profile(request):
     all_data=Album_model.objects.all()
     return render(request,'profile.html',{'data':all_data })


@login_required
def logout_user(request):
    logout(request)
    messages.success(request,'Logged Out success')
    return redirect('login')