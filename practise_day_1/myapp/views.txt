from django.shortcuts import render,redirect
from .forms import SignUp_Form
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUp_Form(request.POST)
            if form.is_valid():
                messages.success(request,'SignUp Suceess')
                form.save()
                return redirect('profile')

        else:
            form=SignUp_Form()
        return render(request,'signuppage.html',{'form':form})
    else:
        return redirect('profile')
    




def login_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request.POST,data=request.POST)
            if form.is_valid():
                usr_name=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=usr_name,password=password)
                if user is not None:
                    messages.success(request,'Login Suceess')
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.warning(request,'Login Failed')
                    return redirect('signup')


        else:
            form=AuthenticationForm()
        return render(request,'loginPage.html',{'form':form})
    else:
        return redirect('profile')
  

@login_required
def profile(request):
     return render(request,'profilepage.html')
    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request,'Logged Out success')
    return redirect('login')



@login_required
def password_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Change Sucess')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'passchangeform.html',{'form':form})
       





@login_required
def password_change_without_old_pass(request):
    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Change Sucess')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
         form=SetPasswordForm(user=request.user)
    return render(request,'passchangeform.html',{'form':form})
  
        

