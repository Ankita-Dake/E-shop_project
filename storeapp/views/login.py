from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from storeapp.models.product import Product
from storeapp.models.category import Category
from storeapp.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None

                    return redirect('homepage')
            else:
                error_message = "email or password invalid"
        else:
            error_message = "email or password invalid"
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
