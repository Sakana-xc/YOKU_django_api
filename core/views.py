from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def store(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        item = Item(name=name, price=price)
        item.save()
        return JsonResponse({"message": "Item saved successfully"})
    return render(request, 'template.html')
