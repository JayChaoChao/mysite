#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
#@author:WDX
#@file: urls.py
# datetime:2019/12/11 11:09
# software: PyCharm
"""
from django.contrib import admin
from django.urls import path,re_path
from mysote import views

app_name='mysote'


urlpatterns = [
	path('',views.index),
	re_path('^(\d+)/(\d+)/$',views.detail),
	re_path('^grade/$',views.grades),
	re_path('^student/$',views.students),
	re_path('^grade/(\d+)/$',views.gradesStudent),
	re_path('^addstu/',views.addstudent),
	re_path('^addstu2/',views.addstudent2),
	re_path('^stupage/(\d+)/$',views.stupage),

	re_path('^stusearch/$',views.stusearch),
	re_path('^attribles/',views.attribles),
	re_path('^get1/',views.get1),
	re_path('^get2/',views.get2),
	re_path('^showregister/register/',views.regist),
	re_path('^showregister/',views.showregister),
	re_path('^cookietest/',views.cookietest),
	re_path('^redirect1/',views.redirect1),
	re_path('^redirect2/',views.redirect2),

	re_path('^main/$',views.main),
	re_path('^login/$',views.login),
	re_path('^showmain/$',views.showmain),
	re_path('^quit/$',views.quit),

	re_path('^good/(\d+)/$',views.good,name='good'),#url反向解析

	re_path('^index/$',views.indexmain),

	re_path('^verifycode/$',views.verifycode),
	re_path('^verifycodefile/',views.codefile),
	re_path('^verifycodecheck/',views.codecheck),

	re_path('^upfile/',views.upfile),
	re_path('^savefile/',views.savefile),

	re_path('^studentpage/(\d+)/$',views.studentpage),
	re_path('^ajaxshowstu/',views.ajaxshowstu),

	re_path('^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/',views.getdate)
]
