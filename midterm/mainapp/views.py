from django.shortcuts import render,redirect
from .models import BrandModel,Car_Model,OrderModel,Comment
from django.views.generic import DetailView
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request,slug=None):
    
    allbrand=BrandModel.objects.all()
    alp=Car_Model.objects.all()

    if slug is not None:
        mdl=BrandModel.objects.get(slug=slug)
        alp=Car_Model.objects.filter(brand=mdl)
      
    return render(request,'mainhero.html',{'data':allbrand,'product':alp})



def details(request, id):
   
    single_car = Car_Model.objects.get(pk=id)
    

    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            alreadyexist= Comment.objects.filter(email=form.cleaned_data['email'],car=single_car)
            if alreadyexist:
                 messages.warning(request,"You have already commented")
        
            else:
                cmnt = form.save(commit=False) 
                cmnt.car = single_car 
                cmnt.save()
                return redirect('details', id=id)


    else:
        form = CommentForm()

    comments = Comment.objects.filter(car_id=id)
    return render(request, 'details.html', {
        'data': single_car,
        'comments': comments,
        'form': form
    })
@login_required
def buy_car(request,id):
    acar=Car_Model.objects.get(pk=id)
    already_buy=OrderModel.objects.filter(user=request.user, car=acar).first()

    if already_buy:        
        already_buy.quantity+=1
        already_buy.total_price+=acar.price        
        already_buy.save()        
    else:
        OrderModel.objects.create(
            user=request.user,
            car=acar,
            quantity=1,
            total_price=acar.price
        ).save()

    acar.quantity-=1    
    acar.save()                   
    return redirect('allorder')


 