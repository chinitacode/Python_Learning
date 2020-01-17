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

### [yield VS yield from](https://juejin.im/post/5b3af9fb51882507d4487144)
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
认真阅读以上代码，应该很容易能理解，调用方、委托生成器、子生成器之间的关系。 
**委托生成器**的作用是：在调用方与子生成器之间建立一个**双向通道**。  
所谓的双向通道是什么意思呢？调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。 
有时还可以在yield from前面看到可以赋值。这是什么用法？ 
你可能会以为，子生成器yield回来的值，被委托生成器给拦截了，但并不是那样。因为我们之前说了，委托生成器，只起一个桥梁作用，它建立的是一个双向通道，它并没有权利也没有办法，对子生成器yield回来的内容做拦截。  
为了解释这个用法，我们还是用上述的例子，并对其进行了一些改造。 

```
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count

    # 每一次return，都意味着当前协程结束。
    return total,count,average

# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)      # 结束协程
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程

if __name__ == '__main__':
    main()

```
运行后，输出: 
```
10.0
15.0
20.0
计算完毕！！
总共传入 3 个数值， 总和：60，平均数：20.0
```
### 为什么要使用yield from 
可能会有疑问：既然委托生成器，起到的只是一个双向通道的作用，那还需要委托生成器做什么？调用方直接调用子生成器不就好了？ 

原因很简单，因为它**可以帮我们处理异常**。 

如果我们去掉委托生成器，而直接调用子生成器。那我们就需要把代码改成像下面这样，我们需要自己捕获异常并处理。而不像使yield from那样省心。 
```
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count
    return total,count,average

# 调用方
def main():
    calc_average = average_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

    # ----------------注意-----------------
    try:
        calc_average.send(None)
    except StopIteration as e:
        total, count, average = e.value
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
    # ----------------注意-----------------

if __name__ == '__main__':
    main()
```
此时的你，可能会说，不就一个StopIteration的异常吗？自己捕获也没什么大不了的。 

你要是知道yield from在背后为我们默默无闻地做了哪些事，你就不会这样说了。 

具体yield from为我们做了哪些事，可以参考如下这段代码。 

```
#一些说明
"""
_i：子生成器，同时也是一个迭代器
_y：子生成器生产的值
_r：yield from 表达式最终的值
_s：调用方通过send()发送的值
_e：异常对象
"""

_i = iter(EXPR)

try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value

else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r
```

[说明]：

迭代器（即可指子生成器）产生的值直接返还给调用者 
任何使用send()方法发给委派生产器（即外部生产器）的值被直接传递给迭代器。如果send值是None，则调用迭代器next()方法；如果不为None，则调用迭代器的send()方法。如果对迭代器的调用产生StopIteration异常，委派生产器恢复继续执行yield from后面的语句；若迭代器产生其他任何异常，则都传递给委派生产器。
子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以它不支持.throw()和.close()方法,即可能会产生AttributeError 异常。
除了GeneratorExit 异常外的其他抛给委派生产器的异常，将会被传递到迭代器的throw()方法。如果迭代器throw()调用产生了StopIteration异常，委派生产器恢复并继续执行，其他异常则传递给委派生产器。 
如果GeneratorExit异常被抛给委派生产器，或者委派生产器的close()方法被调用，如果迭代器有close()的话也将被调用。如果close()调用产生异常，异常将传递给委派生产器。否则，委派生产器将抛出GeneratorExit 异常。 
当迭代器结束并抛出异常时，yield from表达式的值是其StopIteration 异常中的第一个参数。 
一个生成器中的return expr语句将会从生成器退出并抛出 StopIteration(expr)异常。 

所以yield from帮我们做了很多的异常处理，而且全面，而这些如果我们要自己去实现的话，一个是编写代码难度增加，写出来的代码可读性极差，还可能有遗漏，只要哪个异常没考虑到，都有可能导致程序崩溃。 




