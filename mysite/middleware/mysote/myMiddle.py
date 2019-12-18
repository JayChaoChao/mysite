#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
#@author:WDX
#@file: myMiddle.py
# datetime:2019/12/13 16:29
# software: PyCharm
"""

from django.utils.deprecation import MiddlewareMixin
'''
中间件：本质是一个python类
面向切面编程(Aspect Oriented Programming---（AOP)):
1.AOP主要目的是针对业务处理过程中的切面进行处理
2.它所面对的是处理过程中的某个步骤或阶段
3.用来获得逻辑过程中各部分之间低耦合的隔离效果

方法：1.__init__:不需要参数，服务器响应第一个请求时自动调用，用于确认是否调用该中间件
      2.process_request(self,request):在匹配url之前执行，返回None或者HttpResponse对象（可以检测爬虫)
      3.process_view(self,request,view_func,view_arg,view_kwargs):在调用试图之前执行，返回None或者HttpResponse对象
      4.process_template_response(self,request,response)：在试图刚好执行完后调用，返回None或者HttpResponse对象，使用render
      5.process_response(self,response)：在所有响应返回浏览器之前调用，每个强求都会调用
      6.process_exception(self,requset,exception)：试图抛出异常时调用，返回HttpResponse对象
'''
class MyMiddle(MiddlewareMixin):
	def process_request(self,request):
		print("get参数为：",request.GET.get('a'))


