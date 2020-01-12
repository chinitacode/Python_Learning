def count_and_say(n):
    if n == 1:
        return '1'
    tmp = count_and_say(n-1)
    count = 1
    result = ''
    for i in range(len(tmp)):
        if i != len(tmp)-1 and tmp[i] == tmp[i+1]:
            count += 1
        else:
            result += str(count) + tmp[i]
            count = 1
    return result
            
