# coding=utf-8
from models import *
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hashlib import sha1

# Create your views here.

# 显示登陆界面
def login(resquest):
    return render(resquest,'users/login.html')

# 显示注册界面
def register(resquest):
    return render(resquest, 'users/register.html')

# 注册页面用户名邮箱验证
def register_commit(resquest):
    robjects = resquest.GET
    # 获取输入用户名
    ruser = robjects.get('userName','')
    # 获取数据库用户名,没有返回[]
    dbuser = userLogin.objects.filter(user_name=ruser)
    # 获取用户输入email
    remail = robjects.get('userEmail','')
    # 获取数据库中的邮箱
    dbemail = userInfo.objects.filter(email=remail)
    # 判断用户是否存在.存在name=1,否则name=0
    if ruser == dbuser:
        name = 1
    else:
        name = 0

    # 判断邮箱是否存在,存在email=1,否则email=0
    if remail == dbemail:
        email = 1
    else:
        email = 0
    # 构造上下文
    context = {'userName':name,'userEmail':email}
    return JsonResponse(context)

# 注册
def pregister_commit(resquest):
    robjects = resquest.POST
    #获取用户名
    ruser = robjects.get('user_name','')
    #获取输入密码
    rpasswd = robjects.get('pwd','')
    # 获取确认密码
    rcpasswd = robjects.get('cpwd','')
    #密码加密
    s1 = sha1()
    s1.update(rpasswd)
    rpasswd_sha1 = s1.hexdigest()
    #获取邮箱
    remail = robjects.get('email','')
    #存入数据库


# 显示用户信息界面
def info(resquest):
    return render(resquest, 'users/user_center_info.html')

# 显示用户中心订单界面
def order(resquest):
    return render(resquest, 'users/user_center_order.html')

# 显示用户中心地址界面
def site(resquest):
    return render(resquest, 'users/user_center_site.html')

