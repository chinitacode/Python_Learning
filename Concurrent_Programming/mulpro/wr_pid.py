'''
读写pid来判断自身是否正在运行
'''
import os
import psutil
import time

def write_pid(pname):
    pid = os.getpid()
    #print("%s_pid.txt" %pname)
    fp = open("%s_pid.txt" %pname,'w')
    fp.write(str(pid)) #write() argument must be str，只能往文件里面写str
    fp.close()

def read_pid(pname):
    if os.path.exists("%s_pid.txt" %pname):
        fp = open("%s_pid.txt" %pname,'r')
        pid = fp.read().strip()
        fp.close()
        return pid
    else:
        print('File "%s_pid.txt" %pname does not exist')
        return False

def write_log(log_content):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_content = time_now+"---->"+log_content+os.linesep
    fp = open('recognition.log','a+')
    fp.write(log_content)
    fp.close()

def is_running(pname):
    pid = read_pid('%s' %pname)
    if pid:
        #print(pid)
        pid = int(pid)
        running_pid = psutil.pids()
        if pid in running_pid:
            log_content =  '(%s) is running...' %pname
            print(log_content)
            write_log(log_content)
            return True
        else:
            print('(%s) is not running...' %pname)
            return False
    else:
        print('pid of (%s) not written yet' %pname)
        return False

def func(num):
    write_pid('func')
    print(num**2)

if __name__ == "__main__":
    func(3)
    is_running('func')
