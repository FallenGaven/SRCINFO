#coding:utf-8
'''
Created on 2017/11/28

@author: gy071089
'''

from django import forms
from django.forms.widgets import TextInput

class SigninForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30)
    password = forms.CharField(label='密码',max_length=25,widget=forms.PasswordInput())
    widgets = {
                   'username': TextInput(attrs={'class':'form-control','placeholder':'请输入账号'}),
                   'password': TextInput(attrs={'class':'form-control','type':'password','placeholder':'请输入密码'}),
                   }
    
class RegistForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30)
    password = forms.CharField(label='密码',max_length=25,widget=forms.PasswordInput())
    re_password = forms.CharField(label='密码',max_length=25,widget=forms.PasswordInput())
    widgets = {
                   'username': TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
                   'password': TextInput(attrs={'class':'form-control','type':'password','placeholder':'密码'}),
                   're_password': TextInput(attrs={'class':'form-control','type':'password','placeholder':'密码确认'}),
                   }