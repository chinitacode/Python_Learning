### [logging.basicConfig()函数说明](https://www.cnblogs.com/yyds/p/6901864.html)   
该方法用于为logging日志系统做一些基本配置，方法定义如下：   
`logging.basicConfig(**kwargs)`   
该函数可接收的关键字参数如下：   
|  参数名称      |	                 描述                                      |
|---------------|-------------------------------------------------------------|
|filename	|指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了|
|filemode	|指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效|
|format	|指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。|
|datefmt	|指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效|
|level	|指定日志器的日志级别|
|stream	|指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常|
|style	|Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'|
|handlers|Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。|   

#### 注意，basicConfig 只能在运行时第一次调用。如果您已经配置了根 logger ，调用 basicConfig 将不起作用。   

经过配置的日志输出   
先简单配置下日志器的日志级别:   
```
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```

输出结果：
```
DEBUG:root:This is a debug log.
INFO:root:This is a info log.
WARNING:root:This is a warning log.
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log.
所有等级的日志信息都被输出了，说明配置生效了。
```
在配置日志器日志级别的基础上，在配置下日志输出目标文件和日志格式  

```LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```
此时会发现控制台中已经没有输出日志内容了，但是在python代码文件的相同目录下会生成一个名为'my.log'的日志文件，该文件中的内容为：
```
2017-05-08 14:29:53,783 - DEBUG - This is a debug log.
2017-05-08 14:29:53,784 - INFO - This is a info log.
2017-05-08 14:29:53,784 - WARNING - This is a warning log.
2017-05-08 14:29:53,784 - ERROR - This is a error log.
2017-05-08 14:29:53,784 - CRITICAL - This is a critical log.
```

在上面的基础上，我们再来设置下日期/时间格式
```
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```
此时会在my.log日志文件中看到如下输出内容：  
```
05/08/2017 14:29:04 PM - DEBUG - This is a debug log.
05/08/2017 14:29:04 PM - INFO - This is a info log.
05/08/2017 14:29:04 PM - WARNING - This is a warning log.
05/08/2017 14:29:04 PM - ERROR - This is a error log.
05/08/2017 14:29:04 PM - CRITICAL - This is a critical log.
```
掌握了上面的内容之后，已经能够满足我们平时开发中需要的日志记录功能。  
