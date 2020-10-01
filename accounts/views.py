from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderFrom


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    total_customer = customers.count()
    order_delivery = orders.filter(status='Ddelivery').count()
    order_pending = orders.filter(status='Pending').count()
    context = {
        'customers': customers,
        'orders': orders,
        'total_order': total_order,
        'total_customer': total_customer,
        'order_delivery': order_delivery,
        'order_pending': order_pending,

    }
    return render(request, 'accounts/dashboard.html', context)


def customer(request, pk):
    
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_order': total_order,
    }
    return render(request, 'accounts/customer.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/product.html', context)


def create_orders(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset': formset,
    }
    return render(request, 'accounts/create_order.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderFrom(instance=order)
    if request.method == 'POST':
        #   print("print all data",request.POST)
        form = OrderFrom(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/create_order.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order,
    }
    return render(request, 'accounts/delete_order.html', context)
