# -*- coding: utf-8 -*-
import logging

'''
使用工厂方法返回一个Logger实例。
logging.getLogger([name=None])
指定name，返回一个名称为name的Logger实例。如果再次使用相同的名字，是实例化一个对象。未指定name，返回Logger实例，名称是root，即根Logger。
Logger是层次结构的，使用 '.' 点号分割，如'a'、'a.b'或'a.b.c.d'，'a'是'a.b'的父parent，a.b是a的子child。
对于foo来说，名字为foo.bar、foo.bar.baz、foo.bam都是foo的后代。
'''

DATEFMT ="[%Y-%m-%d %H:%M:%S]"
FORMAT = "%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt=DATEFMT,filename='class_test.log')
 
root = logging.getLogger()
print(root.name,type(root),root.parent,id(root))
 
logger = logging.getLogger(__name__)
print(logger.name, type(logger), id(logger), id((logger.parent)))
 
logger1 = logging.getLogger(__name__ + ".ok")
print(logger1.name, type(logger1), id(logger1), id((logger1.parent)))
 
print(logger1.parent,id(logger1.parent))
