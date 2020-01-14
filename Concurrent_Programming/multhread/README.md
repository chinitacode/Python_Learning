在Python3中，通过threading模块提供线程的功能。原来的thread模块已废弃。但是threading模块中有个Thread类（大写的T，类名），是模块中最主要的线程类，一定要分清楚了，千万不要搞混了。 

#### Thread实例对象的方法 
  + isAlive(): 返回线程是否活动的。 
  + getName(): 返回线程名。 
  + setName(): 设置线程名。 

#### threading模块提供的一些方法： 
  + threading.currentThread(): 返回当前的线程变量。 
  + threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
  + threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果 
