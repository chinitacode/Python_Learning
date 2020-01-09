from multiprocessing import Process
import os

class MyProcess(Process): #自己写一个类，继承Process类
    #我们通过init方法可以传参数，如果只写一个run方法，那么没法传参数，因为创建对象的是传参就是在init方法里面，面向对象的时候，我们是不是学过
    def __init__(self,person):
        super().__init__()
        self.person=person
    def run(self):
        print('%s，pid代号%s 正在测试代码' %(self.person,self.pid))

if __name__ == '__main__':
    print('Parent process (%s) starts.' %os.getpid())
    p1=MyProcess('Jedan')
    p2=MyProcess('太白')
    p3=MyProcess('alexDSB')

    p1.start() #start内部会自动调用run方法
    p2.start()
    # p2.run()
    p3.start()


    p1.join()
    p2.join()
    p3.join()
    print('Parent process ends')
