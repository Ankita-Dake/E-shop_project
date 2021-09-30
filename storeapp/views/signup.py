from django.views import View
from storeapp.models.customer import Customer
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        # validation
        if not first_name:
            error_message = "first Name Required!"
        elif len(first_name) < 4:
            error_message = 'first name must be 4 char long and more'
        if not last_name:
            error_message = "last Name Required!"
        elif len(last_name) < 4:
            error_message = 'first name must be 4 char long and more'
        if not phone:
            error_message = "Phone No. Required!"
        elif len(phone) < 10:
            error_message = "Phone Number must be 10 digit"
        elif customer.isExits():
            error_message = 'Email Address already register'

        # saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
