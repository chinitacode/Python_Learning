class A(object):  # -> don't forget the object specified as base

    def __new__(cls):
        print("A.__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("A.__init__ called")

A()
'''
[输出结果]：
A.__new__ called
A.__init__ called

__new__ 是在我们调用类名进行实例化时自动调用的，__init__ 是在这个类的每一次实例化对象之后调用的，
__new__ 方法创建一个实例之后返回这个实例对象并传递给 __init__ 方法的 self 参数。
因此，即使你将创建的实例对象保存成一个全局或静态的变量，
并且每次调用__new__ 方法时都返回这个对象，
__init__ 方法依然每次都会被调用。
这意味着如果我们在 __new__ 中省略调用基类的super(A, cls).__new__(cls) 代码，
__init__ 方法将不会被执行。

示例：
'''
print("--------------------------------",'\n')

class A(object):

    def __new__(cls):
        print ("A.__new__ called")

    def __init__(self):
        print ("A.__init__ called")  # -> is actually never called

A()
'''
[输出结果]：
A.__new__ called

想像一下，如果我们从 __new__ 中返回一些其他东西(对象)将会发生什么，如下面这样：
'''
print("--------------------------------",'\n')

class A(object):

    def __new__(cls):
        print("A.__new__ called")
        return 29

print(A())

print("--------------------------------",'\n')
'''
[输出结果]：
A.__new__ called
29

我们再看一下从 __init__ 中返回一个对象将会发生什么：
'''
class A(object):

    def __init__(self):
        print ("A.__init__ called")
        # return 33  # -> TypeError: __init__ should return None

A()
print("--------------------------------",'\n')

'''
[输出结果]：
A.__init__ called
Traceback (most recent call last):
  File "new.py", line 67, in <module>
    A()
TypeError: __init__() should return None, not 'int'

这主要是因为 __init__ 的作用只是刷新和更改刚创建的这个实例对象的状态。


新式的类在灵活性上提供了更多的功能，允许我们在构造和初始化的级别做更多预处理和后处理的操作，
让我们可以在实例化时控制我们想要返回的内容。

考虑到这一点，我们尝试一下在 __new__ 中返回一个其他类的对象。
'''
class Sample(object):
    def __str__(self):
        return "SAMPLE"

class A(object):
    def __new__(cls):
        return super().__new__(Sample)
print(A())
print("--------------------------------",'\n')

'''
[输出结果]：
SAMPLE

相当于：
class A(object):
    def __new__(cls):
        return Sample()
'''
