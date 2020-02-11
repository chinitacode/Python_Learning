'''
怎么用Python怎么实现Singleton？怎么实现工厂模式？
先来看Singleton：
1.用__new__来实现
'''
class Singleton(object):
    _instance = None # 类属性，即Singleton._instance,也就是cls._instance
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

'''
[输出结果]：
<__main__.Singleton object at 0x7fd4db6b7d68>
<__main__.Singleton object at 0x7fd4db6b7d68>

可以看到s1和s2都指向同一个对象，实现了单例模式。

再来看下工厂模式的实现
'''
class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass

class Apple(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")

class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")

class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]() #返回相应的水果实例
        else:
            return Fruit()

fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit3 = FruitFactory("mango")
fruit4 = FruitFactory("orange")
fruit1.print_color()
fruit2.print_color()
fruit3.print_color()
fruit4.print_color()
print(fruit2 is fruit4)
'''
上面的代码输出

apple is in red
orange is in orange
orange is in orange
false
'''
