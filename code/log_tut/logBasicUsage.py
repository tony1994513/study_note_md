# -*- coding: utf-8 -*-

import logging

'''
配置logging基本的设置，然后在控制台输出日志

logging.basicConfig函数各参数：
filename：指定日志文件名；
filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
format：指定输出的格式和内容，format可以输出很多有用的信息，
'''

logging.basicConfig(filename='example.log',level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")