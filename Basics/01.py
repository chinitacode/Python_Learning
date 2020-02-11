'''
问题1：请问如何修改以下Python代码，使得下面的代码调用类A的show方法？

'''
class A(object):
    def show(self):
        print("base show")

class B(A):
    def show(self):
        print("derived show")

if __name__ == '__main__':
    obj = B()
    obj.show()  # "derived show"

    # solution: 这道题的考点是类继承，只要通过__class__ 方法指定类对象就可以了。补充的代码如下：
    obj.__class__ = A
    obj.show() # "base show"

    print("\n" + "-----------------------------------------" + "\n")


'''
问题2：请问如何修改以下Python代码，使得代码能够运行？

class A(object):
    def __init__(self, a, b):
        self.__a = a;
        self.__b = b;
    def myprint(self):
        print("a=", self.__a, "b=", self.__b)

if __name__ == '__main__':
    a1 = A(10, 20)
    a1.myprint()

    a1(80) # TypeError: 'A' object is not callable

# 答：此题考察得是方法对象，为了能让对象实例能被直接调用，需要实现 __call__ 方法，补充代码如下：
'''
class A(object):
    def __init__(self, a, b):
        self.__a = a;
        self.__b = b;
    def myprint(self):
        print("a =", self.__a, "b =", self.__b)
    def __call__(self, num):
        print("call: ", num + self.__a)

if __name__ == '__main__':
    a1 = A(10, 20)
    a1.myprint()

    a1(80) # call:  90

    print("\n" + "-----------------------------------------" + "\n")


'''
问题3：下面这段代码的输出是什么？
'''
class B(object):
    def fn(self):
        print("B fn")
    def __init__(self):
        print("B INIT")

class A(object):
    def fn(self):
        print("A fn")
    def __new__(cls,a):
        print("NEW",a)
        if a>10:
            return super().__new__(cls) #返回A类实例A()
        return B()
    def __init__(self,a):
        print("INIT",a)

if __name__ == '__main__':
    a1 = A(5)
    a1.fn()
    a2 = A(20)
    a2.fn()

    print("\n" + "-----------------------------------------" + "\n")

'''
[输出结果]：
NEW 5
B INIT
B fn
NEW 20
INIT 20
A fn


问题4：如何添加代码，使得没有定义的方法都调用mydefault方法？

class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.a2 = b
        print("init")

    def mydefault(self):
        print("default")

a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
'''
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.a2 = b
        print("init")

    def mydefault(self):
        print("default")

    def __getattr__(self, name):
        return self.mydefault

if __name__ == '__main__':
    a1 = A(10,20)
    a1.fn1()
    a1.fn2()
    a1.fn3()

    print("\n" + "-----------------------------------------" + "\n")


'''
[输出结果]：
init
default
default
default

此题的考的是Python的默认方法， 只有当没有定义的方法调用时，才会调用方法 __getattr__。
当 fn1 方法传入参数时，我们可以给 mydefault 方法增加一个 *args 不定参数来兼容。
'''
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.a2 = b
        print("init")

    def mydefault(self, *args):
        print("default: " + str(args[0]))

    def __getattr__(self, name):
        print("other fn calling mydefault: ", name)
        return self.mydefault

if __name__ == '__main__':
    a1 = A(10,20)
    a1.fn1(33,44)
    a1.fn2("hello")
    a1.fn3(10)

    print("\n" + "-----------------------------------------" + "\n")


'''
[输出结果]：
init
other fn calling mydefault:  fn1
default: 33
other fn calling mydefault:  fn2
default: hello
other fn calling mydefault:  fn3
default: 10


问题5： 一个包里有三个模块，mod1.py , mod2.py , mod3.py ，
但使用 from demopack import * 导入模块时，如何保证只有 mod1 、 mod3 被导入了。

答:在包中增加 __init__.py 文件，并在文件中增加：

__all__ = ['mod1', 'mod3']


问题6：写一个函数，接收整数参数 n ，返回一个函数，函数返回n和参数的积。
'''
def mulby(num):
    def multiplier(n):
        return num*n
    return multiplier

if __name__ == '__main__':
    mulby7 = mulby(7)
    print(mulby7(8))

    print("\n" + "-----------------------------------------" + "\n")

'''
问题7：请问下面的代码有什么隐患？

def strtest(num):
    s = "first"
    for _ in range(num):
        s += "X"
    return s

答：由于变量str是个不可变对象，每次迭代，python都会生成新的str对象来存储新的字符串，
num越大，创建的str对象越多，内存消耗越大。
'''
