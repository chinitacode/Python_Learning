import types
import functools

def log(text=''):
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text,str) and len(text) != 0:
                print('text 的值为字符串类型')
                print("%s %s()" %(text, func.__name__))
            print("begin call %s()" %(func.__name__))
            result = func(*args, **kw)
            print("end call %s()" %(func.__name__))
            return result
        return wrapper
    
    if isinstance(text, types.FunctionType):
        print('txt: ', text)
        print('text 的值为函数类型')
        return decorator(text)
    else:
        print('txt: ',text)
        print('text的值不为函数类型，无参调用函数')
        return decorator

@log
def now(task):
	print(f'now I\'m {task}')

print('log 无参数:')
print(now('testing'),'\r\n')


@log('Execute')
def now(task):
	print(f'now I\'m {task}')
	
print('With paramter \'Execute\'')
print(now('testing'),'\r\n')


@log()
def now(task):
	print(f'now I\'m {task}')
	
print('Without paramter but with ()')
print(now('testing'),'\r\n')
