# -*- coding: utf-8 -*-
import logging
 
FORMAT = "%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.WARNING,format=FORMAT,datefmt="[%Y-%m-%d %H:%M:%S]")
 
root = logging.getLogger()
print(1,root,id(root)) #RootLogger,根Logger
root.info('my root') #低于定义的WARNING级别，所以不会记录
 
loga = logging.getLogger(__name__) #Logger继承自RootLogger
print(2,loga,id(loga),id(loga.parent))
print(3,loga.getEffectiveLevel()) #数值形式的有效级别
loga.setLevel(level=logging.DEBUG)
print(4,loga.getEffectiveLevel()) #数值形式的有效级别
loga.warning('before')
print(5,loga.getEffectiveLevel())
loga.info('after')#
loga.warning('after1')