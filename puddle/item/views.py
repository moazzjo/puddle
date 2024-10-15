from django.shortcuts import render, get_object_or_404, redirect
from item import models

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from .forms import  newItemForm, EditItemForm

# Create your views here.


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category',0)
    categories = models.Category.objects.all()
    items = models.Item.objects.filter(is_sold= False)

    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description_icontains=query) )

    return render(request, 'item/item.html', {
        'items':items,
        'query':query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    item = get_object_or_404(models.Item, pk=pk)
    related_items= models.Item.objects.filter(category=item.category, is_sold = False).exclude(pk=pk)[0:3]

    return render(request,'item/detail.html', {
        "item": item,
        "related_items": related_items
    })

@login_required
def new(request):

    if request.method == "POST":
        form = newItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit= False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
        
    else:

        form = newItemForm()


    return render(request, 'item/form.html',{
        'form': form,
        'title': 'new item'
     })

@login_required
def edit(request, pk):
    item = get_object_or_404(models.Item, pk=pk)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

            return redirect('item:detail', pk=item.id)
        
    else:

        form = EditItemForm(instance=item)


    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edit item'
     })


@login_required
def delete(request, pk):
    item = get_object_or_404(models.Item, pk=pk, created_by = request.user)
    item.delete()

    return redirect('dashboard:index')