'''
实现场景：
总共有14个鱼丸，
当a同学向火锅里面添加鱼丸加满后（最多5个，加满后通知b去吃掉），
通知b同学去吃掉鱼丸（吃到0的时候通知a同学继续添加）
'''
import threading, time

# 生产者
class Producer(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        # 锁定线程
        global num, total
        con.acquire()
        while True:
            print ("开始添加！！！")
            num += 1
            total -= 1
            print( "火锅里面鱼丸个数：%s" % str(num))
            time.sleep(0.2)
            if total == 0:
                print('鱼丸已全部加完。')
                con.notify()
                break
            if num >= 5:
                print ("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
                # 等待通知
                con.wait()
        # 释放锁
        con.release()

# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        con.acquire()
        global num
        while True:
            print( "开始吃啦！！！")
            if num > 0: num -= 1
            print ("火锅里面剩余鱼丸数量：%s" %str(num))
            time.sleep(0.5)
            if num <= 0:
                if total == 0:
                    print('鱼丸已全部吃完。')
                    break
                print ("锅底没货了，赶紧加鱼丸吧！")
                con.notify()  # 唤醒其它线程
                # 等待通知
                con.wait()
        con.release()
if __name__ == '__main__':
    total = 14 # 鱼丸总数
    num = 0
    con = threading.Condition()
    p = Producer()
    c = Consumers()
    c.start()
    p.start()
    '''
    【输出结果】：
    开始吃啦！！！
    火锅里面剩余鱼丸数量：0
    锅底没货了，赶紧加鱼丸吧！
    开始添加！！！
    火锅里面鱼丸个数：1
    开始添加！！！
    火锅里面鱼丸个数：2
    开始添加！！！
    火锅里面鱼丸个数：3
    开始添加！！！
    火锅里面鱼丸个数：4
    开始添加！！！
    火锅里面鱼丸个数：5
    火锅里面里面鱼丸数量已经到达5个，无法添加了！
    开始吃啦！！！
    火锅里面剩余鱼丸数量：4
    开始吃啦！！！
    火锅里面剩余鱼丸数量：3
    开始吃啦！！！
    火锅里面剩余鱼丸数量：2
    开始吃啦！！！
    火锅里面剩余鱼丸数量：1
    开始吃啦！！！
    火锅里面剩余鱼丸数量：0
    锅底没货了，赶紧加鱼丸吧！
    开始添加！！！
    火锅里面鱼丸个数：1
    开始添加！！！
    火锅里面鱼丸个数：2
    开始添加！！！
    火锅里面鱼丸个数：3
    开始添加！！！
    火锅里面鱼丸个数：4
    开始添加！！！
    火锅里面鱼丸个数：5
    火锅里面里面鱼丸数量已经到达5个，无法添加了！
    开始吃啦！！！
    火锅里面剩余鱼丸数量：4
    开始吃啦！！！
    火锅里面剩余鱼丸数量：3
    开始吃啦！！！
    火锅里面剩余鱼丸数量：2
    开始吃啦！！！
    火锅里面剩余鱼丸数量：1
    开始吃啦！！！
    火锅里面剩余鱼丸数量：0
    锅底没货了，赶紧加鱼丸吧！
    开始添加！！！
    火锅里面鱼丸个数：1
    开始添加！！！
    火锅里面鱼丸个数：2
    开始添加！！！
    火锅里面鱼丸个数：3
    开始添加！！！
    火锅里面鱼丸个数：4
    鱼丸已全部加完。
    开始吃啦！！！
    火锅里面剩余鱼丸数量：3
    开始吃啦！！！
    火锅里面剩余鱼丸数量：2
    开始吃啦！！！
    火锅里面剩余鱼丸数量：1
    开始吃啦！！！
    火锅里面剩余鱼丸数量：0
    鱼丸已全部吃完。
    '''
