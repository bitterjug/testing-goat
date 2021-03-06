from django.shortcuts import (
    render,
    redirect
)

from .models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/unique-list/')
    else:
        return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(
        request,
        'list.html',
        {'items': items}
    )
