from django.shortcuts import render

# Create your views here.


def login(resquest):
    return render(resquest,'/users/login.html')
