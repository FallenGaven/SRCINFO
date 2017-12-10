#coding:utf-8
'''
Created on 2017/11/28

@author: gy071089
'''


from django.conf.urls import url

from UserManage import views

urlpatterns = [
    url(r'^$', views.signin, name='signin'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^signout/$', views.signout, name='signout'),
]