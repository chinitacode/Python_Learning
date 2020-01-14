在Python3中，通过threading模块提供线程的功能。原来的thread模块已废弃。但是threading模块中有个Thread类（大写的T，类名），是模块中最主要的线程类，一定要分清楚了，千万不要搞混了。 

对于Thread类，它的定义如下： 

threading.Thread(self, group=None, target=None, name=None,  
     args=(), kwargs=None, *, daemon=None) 
- 参数group是预留的，用于将来扩展； 
- 参数target是一个可调用对象，在线程启动后执行； 
- 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。 
- 参数args和kwargs分别表示调用target时的参数列表和关键字参数。 


#### Thread实例对象的方法 
  + isAlive(): 返回线程是否活动的。 
  + getName(): 返回线程名。 
  + setName(): 设置线程名。 

#### threading模块提供的一些方法： 
  + threading.currentThread(): 返回当前的线程变量。 
  + threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
  + threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果 

|方法与属性	   |说明                                   |
|:-------------|:------------------------------------- |
|start()	|启动线程，等待CPU调度|
|run()	|线程被cpu调度后自动执行的方法|
|getName()、setName()和name	|用于获取和设置线程的名称。|
|setDaemon()	|设置为后台线程或前台线程（默认是False，前台线程）。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止。如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程执行完成后，程序才停止。|
|ident	|获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。|
|is_alive()/isAlive()	|判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断这段时间内，线程是激活的。|
|isDaemon()方法和daemon属性	|是否为守护线程|
|join([timeout])	|调用该方法将会使主调线程堵塞，直到被调用线程运行结束或超时。参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。| 

在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务,所以需要用join()或者锁来同步。
