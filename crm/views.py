from django.shortcuts import render, redirect
from .models import Order
from .form import OrderForm


def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'object_list': object_list, 'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    if OrderForm(request.POST).is_valid():
        order = Order(order_name=name, order_phone=phone)
        order.save()
        # return render(request, './', {'name': name, 'phone': phone})
        response = redirect('/?status=success')
        return response
    else:
        response = redirect('/?status=failure')
        return response
