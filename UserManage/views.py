#coding:utf-8

from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_protect
from .forms import SigninForm,RegistForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse


# Create your views here.

@csrf_protect
def signin(request):
    if request.method == 'POST':
        sf = SigninForm(request.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            password = sf.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/SRC/')
    else:
        sf = SigninForm()
    return render(request,'UserManage/login.html',{'sf':sf})

@csrf_protect
def regist(request):
    if request.method == 'POST':
        rf = RegistForm(request.POST)
        if rf.is_valid():
            username = rf.cleaned_data['username']
            password = rf.cleaned_data['password']
            re_password = rf.cleaned_data['re_password']
            if password and password == re_password:
                if username:
                    user = auth.authenticate(username = username,password = password)
                    if user:
                        context = '用户已存在。请重试'
                        return render(request, 'UserManage/regist.html', context)
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponse('无效请求')
            else:
                context = '请校验密码输入是否正确'
                return render(request, 'UserManage/regist.html', context)
    else:
        rf = RegistForm()
    return render(request,'UserManage/regist.html',{'sf':rf})

@login_required
def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')