#coding:utf-8
from django.db import models
import webbrowser

# Create your models here.

#公司信息
class CompanyInfo(models.Model):
    #企业信息
    company_id = models.IntegerField('企    业    编    号')
    company_src_name = models.CharField('应急响应中心',max_length = 50)
    company_src_www = models.URLField('应急中心地址')
    company_name = models.CharField('企业名称',max_length = 50)
    company_www = models.URLField('官网地址')
    company_ioc = models.URLField('企业图标',null=True)
    company_starttime = models.DateField('添加时间',auto_now_add=True)
    company_updatetime = models.DateField('更新时间',auto_now=True)
    
    def __str__(self):
        return str(self.company_id)
    
#子域名信息    
class Subdomain(models.Model):
    #子域名信息
    subdomain_id = models.CharField('子域名编号',max_length=50)
    subdomain_name = models.CharField('子域名名称',max_length=50,null=True)
    subdomain_www = models.URLField('子域名地址')
    subdomain_starttime = models.DateField('添加时间',auto_now_add=True)
    subdomain_updatetime = models.DateField('更新时间',auto_now=True)
    
    subdomain_company = models.ForeignKey(CompanyInfo,related_name='subdomain_in_company')
    
    def __str__(self):
        return str(self.subdomain_www)

#网站信息    
class Webinfo(models.Model):
    web_id = models.CharField('网页编号',max_length=50)
    web_url = models.URLField('网页链接',null=True)
    web_front = models.CharField('前端语言',max_length=30,null=True)
    web_language = models.CharField('开发语言',max_length=30,null=True)
    web_framework = models.CharField('开发框架',max_length=30,null=True)
    web_template = models.CharField('网站模板',max_length=30,null=True)
    web_container = models.CharField('WEB容器',max_length=30,null=True)
    web_starttime = models.DateField('添加时间',auto_now_add=True)
    web_updatetime = models.DateField('更新时间',auto_now=True)
    
    web_subdomain = models.ForeignKey(Subdomain,related_name='web_in_subdomain')
    
    def __str__(self):
        return str(self.web_url)
    
#服务器信息    
class Server(models.Model):
    server_name = models.CharField('服务器名称',max_length=50,null=True)
    server_ip = models.GenericIPAddressField('服务器IP')
    server_os = models.CharField('操作系统',max_length=30,null=True)
    server_starttime = models.DateField('添加时间',auto_now_add=True)
    server_updatetime = models.DateField('更新时间',auto_now=True)
    
    server_company = models.ForeignKey(CompanyInfo,related_name='server_in_company')
    server_subdomain = models.ForeignKey(Subdomain,related_name='server_in_subdomain')
    
    def __str__(self):
        return str(self.server_ip)

#端口 信息    
class Port(models.Model):
    #端口信息模型
    name = models.CharField('应用名称',max_length=30,null=True)
    port = models.CharField('开放端口',max_length=30)
    product = models.CharField('对应服务',max_length=30,null=True)
    version = models.CharField('应用版本',max_length=30,null=True)
    cpe = models.CharField('终端说明',max_length=30,null=True)
    
    port_server = models.ForeignKey(Server,related_name='port_in_server',verbose_name='服务器关联')
    
    def __str__(self):
        return str(self.port)
    
#端口 信息    
class Plug(models.Model):
    #端口信息模型
    plug_name = models.CharField('组件名称',max_length=30)
    plug_version = models.CharField('组件版本',max_length=30,null=True)
    plug_starttime = models.DateField('添加时间',auto_now_add=True)
    plug_updatetime = models.DateField('更新时间',auto_now=True)
    
    plug_webinfo = models.ForeignKey(Webinfo,related_name='plug_in_webinfo',verbose_name='网页关联')
    
    def __str__(self):
        return str(self.plug_name)
    