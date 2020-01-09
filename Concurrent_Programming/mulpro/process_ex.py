'''
模拟两个应用场景：
1、同时对一个文件进行写操作
2、同时创建多个文件
'''
import time,os,re
from multiprocessing import Process
'''
#1.多进程同时对一个文件进行写操作
def func(x,y,i): #'a'表示在原文本的基础上添加内容（如果文件不存在，则创建）
    with open(x,'a',encoding='utf-8') as f:
        print('当前进程%s拿到的文件的光标位置>>%s'%(os.getpid(),f.tell()))
        f.write(y)
'''

#多进程同时创建多个文件
def func(x, y):
    with open(x, 'w', encoding='utf-8') as f:
        f.write(y)

if __name__ == '__main__':

    p_list= []
    for i in range(5):
        #p = Process(target=func,args=('to_do_list.txt','Thing%s\n'%i,i))
        p = Process(target=func,args=('list%s.txt'%i,'The %sst list'%i))
        p_list.append(p)
        p.start()

    [ap.join() for ap in p_list] #这就是个for循环，只不过用列表生成式的形式写的
    #with open('to_do_list.txt','r',encoding='utf-8') as f:
        #data = f.read()
        #all_num = re.findall('\d+',data) #打开文件，统计一下里面有多少个数据，每个数据都有个数字，所以re匹配一下就行了
        #print('>>>>>',all_num,'.....%s'%(len(all_num)))
    print('All files created and written！')
