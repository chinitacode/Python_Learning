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

### yield VS. yield from: 
yield from 是在Python3.3才出现的语法。所以这个特性在Python2中是没有的。

yield from 后面需要加的是可迭代对象，它可以是普通的可迭代对象，也可以是迭代器，甚至是生成器。

yield from 其实就是等待另外一个协程的返回。 

简单应用：拼接可迭代对象 
```
def func():
    for i in range(10):
        yield i

print(list(func()))
```
可以写成： 
```
def func():
    yield from range(10)

print(list(func()))
```
或者： 
```
# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        for i in item:
            yield i

new_list=gen(astr, alist, adict， agen)
print(list(new_list))
# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]
```
使用yield from 
```
# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        yield from item

new_list=gen(astr, alist, adict, agen)
print(list(new_list))
# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]
```
由上面两种方式对比，可以看出，yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁，结构更加清晰。 

### 复杂应用：生成器的嵌套: 
当 yield from 后面加上一个生成器后，就实现了生成的嵌套。 
当然实现生成器的嵌套，并不是一定必须要使用yield from，而是使用yield from可以让我们避免让我们自己处理各种料想不到的异常，而让我们专注于业务代码的实现。 
如果自己用yield去实现，那只会加大代码的编写难度，降低开发效率，降低代码的可读性。既然Python已经想得这么周到，我们当然要好好利用起来。 
讲解它之前，首先要知道这个几个概念: 

>1、调用方：调用委派生成器的客户端（调用方）代码 
>2、委托生成器：包含yield from表达式的生成器函数 
>3、子生成器：yield from后面加的生成器函数 

实例： 
实现实时计算平均值： 
比如，第一次传入10，那返回平均数自然是10. 
第二次传入20，那返回平均数是(10+20)/2=15 
第三次传入30，那返回平均数(10+20+30)/3=20 
```
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()

```



