from django.shortcuts import render
from .models import ShoppingItem
from django.http import JsonResponse

# Create your views here.
def myList(request):
    if request.method == 'POST':
        print(request.POST['name'])
        ShoppingItem.objects.create(name = request.POST['name'])
        name = request.POST['name']
        new_item = ShoppingItem.objects.create(name=name)
        return JsonResponse({'id': new_item.id, 'name': new_item.name})
    
    allItems = ShoppingItem.objects.all()
    return render(request, 'shopping_list.html',{'all_items': allItems})