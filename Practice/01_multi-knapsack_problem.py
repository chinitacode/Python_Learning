weight = [3,2,6,7,1,4,9,5]
value = [6,3,5,8,3,1,6,9]
N = [3,5,1,9,3,5,6,8]#每种物品的个数
target = 20 #The capacity of the knapsack
DP = [0] * (target+1)
n = len(weight)

def UnboundedKnapsack(weight,value):
    for j in range(weight,target+1):
        DP[j] = max(DP[j],DP[j-weight] + value)

def OneZeroKnapsack(weight,value):
    for j in range(target, weight-1, -1):
        DP[j] = max(DP[j],DP[j-weight] + value)

def MultiKnapsack(weight,value,count):
        if (weight * count) >= target:#当该种物品的个数乘以体积大于背包容量，视为有无限个即完全背包
            UnboundedKnapsack(weight,value)
            return
        temp_count = 1  #以上情况不满足，转化为以下情况，具体参考《背包九讲》多重背包的时间优化
        while temp_count < count:
            OneZeroKnapsack(temp_count*weight,temp_count*value)
            count = count - temp_count
            temp_count = temp_count * 2  #转化为1，2，4
        OneZeroKnapsack(count*weight,count*value) #9个中剩下两个

for i in range(n):
    MultiKnapsack(weight[i],value[i],N[i])
print(DP[target])



