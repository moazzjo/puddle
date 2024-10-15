from django.shortcuts import render, redirect

from item import models
from .forms import SignupFrom

# Create your views here.


def index(request):
    items = models.Item.objects.filter(is_sold = False)[0:6]
    categories = models.Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items': items
    })


def contact(request):
    return render(request, 'core/contact.html' )


def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:  
        form = SignupFrom

    return render(request, 'core/signup.html',{'form':form})


