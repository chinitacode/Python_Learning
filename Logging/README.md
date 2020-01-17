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
