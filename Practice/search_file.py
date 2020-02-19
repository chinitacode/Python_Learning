'''
编写一个程序，
能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出相对路径
'''
import os



def search_file(dir,sname): 
    if sname in os.path.split(dir)[1]: #不管是file还是dir,先检验文件名里是否包含sname 
        print(os.path.relpath(dir)) #打印相对路径，相对指相对于当前路径,如果要打绝对路径，直接加上刚开始传入的dir的绝对路径就是了
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return 

    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名 
        search_file(os.path.join(dir,dire),sname) #jion一下就变成了当前文件的绝对路径
                                           # 对每个子目录路劲执行同样的操作


if __name__ == '__main__':
    s = input('Please enter the key word to search files: \n')
    search_file(os.path.abspath('.'),s)
    
