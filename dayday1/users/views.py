from django.shortcuts import render

# Create your views here.


def login(resquest):
    return render(resquest,'users/login.html')

def register(resquest):
    return render(resquest, 'users/register.html')

def info(resquest):
    return render(resquest, 'users/user_center_info.html')

def order(resquest):
    return render(resquest, 'users/user_center_order.html')

def site(resquest):
    return render(resquest, 'users/user_center_site.html')
