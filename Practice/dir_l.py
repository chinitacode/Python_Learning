import time
import os
filelist = [x for x in os.listdir('.') if os.path.isfile(x)]#找到当前目录的文件类型的文件。
path = os.path.abspath('.')

def get_user_name():
    return os.environ['LOGNAME']#environ是个包含很多环境信息的字典，key为LOGNAME对应的value就是username了

def get_file_time(filename):
    filepath = os.path.join(path,filename)
    localtime = time.localtime(os.path.getatime(filepath))
    return time.asctime(localtime)

def get_file_size(filename):
#先把文件用二进制读入再计算大小，非常蠢，开销很大，系统应该有接口可以读入文件的大小信息，不用计算。现在不知道，先不管。
    with open(filename,'rb') as f:
        return(len(f.read()))
for f in filelist:
    print(get_user_name(),get_file_time(f),get_file_size(f) ,f)
