 #this is a Python library
def time_execution(code):
    start = time.clock() # start the clock
    result = eval(code) # evaluate any string as if it is a Python command
    run_time = time.clock() - start # find difference in start and end time
    return result, run_time # return the result of the code and time taken

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
