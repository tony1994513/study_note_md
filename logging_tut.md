## logging 

### 1、日志级别
```
import logging  # 引入logging模块
# 将信息打印到控制台上
logging.debug(u"debug")
logging.info(u"info")
logging.warning(u"warning")
logging.error(u"error")
logging.critical(u"critical")
```
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG 
- debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

- info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

- warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

- error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

- critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行

## 2、部分名词解释
Logging.Formatter：这个类配置了日志的格式，在里面自定义设置日期和时间，输出日志的时候将会按照设置的格式显示内容。

Logging.Logger：Logger是Logging模块的主体，进行以下三项工作：

- 为程序提供记录日志的接口
- 判断日志所处级别，并判断是否要过滤
- 根据其日志级别将该条日志分发给不同handler

常用函数有：

- Logger.setLevel() 设置日志级别
- Logger.addHandler() 和 Logger.removeHandler() 添加和删除一个Handler
- Logger.addFilter() 添加一个Filter,过滤作用
- Logging.Handler：Handler基于日志级别对日志进行分发，如设置为WARNING级别的Handler只会处理WARNING及以上级别的日志。
	- 常用函数有：
		- setLevel() 设置级别
		- setFormatter() 设置Formatter

## 3、日志输出-控制台
```
import logging  # 引入logging模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
```
## 4、日志输出-文件
```
import logging  # 引入logging模块
import os.path
import time
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.path.realpath(__file__))
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
```
- return the absolute path of this file
```
dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
```
- create a new dir if there isn't 
```
if not os.path.isdir(latest_model_folder):
	os.makedirs(latest_model_folder)
```
## 5、日志输出-控制台和文件
```
只要在输入到日志中的第二步和第三步插入一个handler输出到控制台：
创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
第四步和第五步分别加入以下代码即可
ch.setFormatter(formatter)
logger.addHandler(ch)
```
## 7、捕捉异常,用traceback记录
```
import os.path
import time
import logging
# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
# 使用logger.XX来记录错误,这里的"error"可以根据所需要的级别进行修改
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True)
```