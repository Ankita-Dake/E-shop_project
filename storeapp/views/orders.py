from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from storeapp.middlewares.auth import auth_middleware
from storeapp.models.customer import Customer
from storeapp.models.product import Product
from storeapp.models.orders import Order
from django.views import View


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders': orders})
