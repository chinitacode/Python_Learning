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
    # calc_average.send(None) 会返回错误：StopIteration: (60, 3, 20.0)

    # ----------------注意-----------------
    try:
        calc_average.send(None)
    except StopIteration as e:
        total, count, average = e.value
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
    # ----------------注意-----------------

if __name__ == '__main__':
    main()
    '''
    10.0
    15.0
    20.0
    计算完毕！！
    总共传入 3 个数值， 总和：60，平均数：20.0
    '''
