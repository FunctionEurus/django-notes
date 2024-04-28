from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    # if request.method == 'POST':
        # return HttpResponse(request.POST['item_text'])
        # new_item_text = request.POST['item_text']
        # Item.objects.create(text=request.POST['item_text'])
        # return redirect('/lists/the-new-page')
    # else:
    #     new_item_text = ''
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    return render(request, 'home.html')

def view_list(request, list_id):
    list_user = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_user})

def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')

def add_item(request, list_id):
    list_user = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')