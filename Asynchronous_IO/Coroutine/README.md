每个生成器都可以执行send()方法，为生成器内部的yield语句发送数据。此时yield语句不再只是yield xxxx的形式，还可以是var = yield xxxx的赋值形式。它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数，并将这个值赋值给var变量: 
```
def simple_coroutine():
    print('-> 启动协程')
    y = 10
    x = yield y
    print('-> 协程接收到了x的值:', x)
    
    
>>> my_coro = simple_coroutine()
>>> ret = next(my_coro)
-> 启动协程
>>> ret
10
>>> my_coro.send(20)
-> 协程接收到了x的值: 20
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    my_coro.send(20)
StopIteration 
```
因为simple_coroutine函数里没有写循环，只能yield一次，因此两次激活生成器则会报错StopIteration。 


协程可以处于下面四个状态中的一个。当前状态可以导入inspect模块，使用inspect.getgeneratorstate(...) 方法查看，该方法会返回下述字符串中的一个。 

* 'GEN_CREATED'　　等待开始执行。 

* 'GEN_RUNNING'　　协程正在执行。 

* 'GEN_SUSPENDED' 在yield表达式处暂停。 

* 'GEN_CLOSED' 　　执行结束。 

### 【注意！】 
因为send()方法的参数会成为暂停的yield表达式的值，所以，仅当协程处于暂停状态时才能调用 send()方法，例如my_coro.send(10)。
不过，如果协程还没激活（状态是'GEN_CREATED'），就立即把None之外的值发给它，会出现TypeError。
因此，始终要先调用next(my_coro)激活协程（也可以调用my_coro.send(None)），这一过程被称作**预激活**。 

除了send()方法，其实还有throw()和close()方法： 

generator.throw(exc_type[, exc_value[, traceback]]) 
使生成器在暂停的yield表达式处抛出指定的异常。如果生成器处理了抛出的异常，代码会向前执行到下一个yield表达式，
而产出的值会成为调用generator.throw()方法得到的返回值。如果生成器没有处理抛出的异常，异常会向上冒泡，传到调用方的上下文中。 

generator.close() 
使生成器在暂停的yield表达式处抛出GeneratorExit异常。如果生成器没有处理这个异常，
或者抛出了StopIteration异常（通常是指运行到结尾），调用方不会报错。
如果收到GeneratorExit异常，生成器一定不能产出值，否则解释器会抛出RuntimeError异常。生成器抛出的其他异常会向上冒泡，传给调用方。 

