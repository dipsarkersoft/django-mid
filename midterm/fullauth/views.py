from django.shortcuts import render,redirect
from .forms import Register_User,ChangeUserForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from mainapp.models import OrderModel
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=Register_User(request.POST)
            if form.is_valid():
                messages.success(request,'SignUp Suceess')
                form.save()
                return redirect('login')

        else:
            form=Register_User()
        return render(request,'signup.html',{'form':form})
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
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile') 
        return super().dispatch(request, *args, **kwargs)
    

@login_required
def profile(request):   
     return render(request,'profile.html')

@method_decorator(login_required, name='dispatch')
class AllOrderView(ListView):
    model = OrderModel
    template_name = 'myorder.html'  
    context_object_name = 'data'  

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)

@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_form =ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form =ChangeUserForm(instance = request.user)
    return render(request, 'editprofile.html', {'form' : profile_form})

@method_decorator(login_required, name='dispatch')
class PassChangeView(PasswordChangeView):
    template_name = 'changepass.html'
    success_url = reverse_lazy('profile')
