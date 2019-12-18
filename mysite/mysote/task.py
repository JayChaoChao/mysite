#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
#@author:WDX
#@file: task.py
# datetime:2019/12/14 13:51
# software: PyCharm
"""
from celery import task
import time

def fun():
	"耗时操作放入celery任务队列中"
	return None