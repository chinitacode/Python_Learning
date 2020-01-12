import time
def singing_score(values):
    ## your code starts here
    lowest,highest = values[0],values[0]
    for i in range(1,len(values)):
        if lowest > values[i]:
            lowest = values[i]
        if highest < values[i]:
            highest = values[i]
    print(lowest,highest)
    values.remove(lowest)
    print(values)
    values.remove(highest)
    aver = sum(values)/len(values)
    return values

   
